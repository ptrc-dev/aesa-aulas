"""
=============================================================================
SIMULADOR GRÁFICO INTERATIVO DE ALGORITMOS DE ORDENAÇÃO (TKINTER GUI)
=============================================================================

Interface gráfica didática para exibição em sala de aula ou estudo individual.
Utiliza a biblioteca padrão Tkinter (não requer nenhuma instalação via pip).

Recursos:
- Visualização gráfica em barras verticais com animação fluida.
- Suporte a todos os 6 algoritmos de ordenação:
    * Bubble Sort
    * Insertion Sort
    * Selection Sort
    * Merge Sort
    * Quick Sort
    * Heap Sort
- Controles interativos:
    * Iniciar / Pausar / Continuar
    * Avanço Passo a Passo (Manual - tecla ou botão)
    * Embaralhar / Gerar Novo Vetor
    * Controle de Velocidade em tempo real (slider)
    * Ajuste do Tamanho do Vetor (10 a 80 barras)
- Indicadores em tempo real:
    * Contador de comparações
    * Contador de trocas / atribuições
    * Descrição do passo atual
    * Complexidade teórica do algoritmo selecionado

Como executar:
    python3 Algoritmos/animacao_gui.py
"""

import os
import sys
import random
import tkinter as tk
from tkinter import ttk

# Suprime aviso de depreciação do Tk no macOS
os.environ["TK_SILENCE_DEPRECATION"] = "1"

# Adiciona o diretório atual ao sys.path para importar os geradores
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from animacao_terminal import (
    anim_bubble_sort,
    anim_insertion_sort,
    anim_selection_sort,
    anim_merge_sort,
    anim_quick_sort,
    anim_heap_sort,
)

# Paleta de Cores Didática
COR_FUNDO = "#1e1e2e"          # Fundo escuro moderno
COR_PAINEL = "#252538"         # Painel de controles
COR_BARRA_PADRAO = "#89b4fa"   # Azul suave (aguardando)
COR_COMPARA = "#f9e2af"        # Amarelo/Dourado (comparando)
COR_TROCA = "#f38ba8"          # Vermelho suave (trocando)
COR_PIVO = "#cba6f7"           # Roxo / Magenta (pivô / chave)
COR_CONCLUIDO = "#a6e3a1"      # Verde (ordenado)
COR_TEXTO = "#cdd6f4"          # Texto claro
COR_TEXTO_MUTED = "#a6adc8"    # Texto secundário

INFOS_ALGORITMOS = {
    "Bubble Sort": {
        "func": anim_bubble_sort,
        "complexidade": "Tempo: O(n²) Médio | O(n) Melhor | Espaço: O(1) | Estável: Sim",
        "resumo": "Compara pares adjacentes e flutua os maiores para o fim."
    },
    "Insertion Sort": {
        "func": anim_insertion_sort,
        "complexidade": "Tempo: O(n²) Médio | O(n) Melhor | Espaço: O(1) | Estável: Sim",
        "resumo": "Insere cada chave na sua posição correta na sublista ordenada."
    },
    "Selection Sort": {
        "func": anim_selection_sort,
        "complexidade": "Tempo: O(n²) Todos os Casos | Espaço: O(1) | Estável: Não",
        "resumo": "Localiza o menor elemento e o troca para o início (mínimo de trocas)."
    },
    "Merge Sort": {
        "func": anim_merge_sort,
        "complexidade": "Tempo: O(n log n) Garantido | Espaço: O(n) | Estável: Sim",
        "resumo": "Divisão e conquista: divide recursivamente e intercala ordenado."
    },
    "Quick Sort": {
        "func": anim_quick_sort,
        "complexidade": "Tempo: O(n log n) Médio | O(n²) Pior | Espaço: O(log n) | Estável: Não",
        "resumo": "Particiona os dados ao redor de um pivô (menores à esq, maiores à dir)."
    },
    "Heap Sort": {
        "func": anim_heap_sort,
        "complexidade": "Tempo: O(n log n) Garantido | Espaço: O(1) | Estável: Não",
        "resumo": "Estrutura de Max-Heap em array: extrai a raiz maior repetidamente."
    },
}


class VisualizadorOrdenacaoGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulador Didático de Algoritmos de Ordenação - AESA")
        self.root.geometry("1000x700")
        self.root.minsize(850, 550)
        self.root.configure(bg=COR_FUNDO)

        # Estado da Aplicação
        self.tamanho_vetor = 30
        self.dados = []
        self.gerador = None
        self.em_execucao = False
        self.pausado = False
        self.job_after = None

        self._criar_interface()
        self.gerar_novos_dados()

    def _criar_interface(self):
        # 1. Topo: Painel de Controles
        painel_topo = tk.Frame(self.root, bg=COR_PAINEL, padx=15, pady=12)
        painel_topo.pack(side=tk.TOP, fill=tk.X)

        # Seletor de Algoritmo
        lbl_alg = tk.Label(painel_topo, text="Algoritmo:", bg=COR_PAINEL, fg=COR_TEXTO, font=("Helvetica", 11, "bold"))
        lbl_alg.grid(row=0, column=0, sticky="w", padx=(0, 6), pady=4)

        self.combo_algoritmo = ttk.Combobox(
            painel_topo,
            values=list(INFOS_ALGORITMOS.keys()),
            state="readonly",
            width=16,
            font=("Helvetica", 11)
        )
        self.combo_algoritmo.current(0)
        self.combo_algoritmo.grid(row=0, column=1, padx=(0, 15), pady=4)
        self.combo_algoritmo.bind("<<ComboboxSelected>>", self._ao_mudar_algoritmo)

        # Botão Iniciar / Pausar
        self.btn_iniciar = tk.Button(
            painel_topo, text="▶ Iniciar", bg="#a6e3a1", fg="#11111b",
            font=("Helvetica", 10, "bold"), relief=tk.FLAT, padx=12, pady=4,
            command=self.alternar_iniciar_pausa, cursor="hand2"
        )
        self.btn_iniciar.grid(row=0, column=2, padx=4)

        # Botão Passo Único (Step)
        self.btn_passo = tk.Button(
            painel_topo, text="⏭ Passo", bg="#cba6f7", fg="#11111b",
            font=("Helvetica", 10, "bold"), relief=tk.FLAT, padx=10, pady=4,
            command=self.avancar_passo_unico, cursor="hand2"
        )
        self.btn_passo.grid(row=0, column=3, padx=4)

        # Botão Novo Vetor / Embaralhar
        self.btn_embaralhar = tk.Button(
            painel_topo, text="🔀 Embaralhar", bg="#89b4fa", fg="#11111b",
            font=("Helvetica", 10, "bold"), relief=tk.FLAT, padx=10, pady=4,
            command=self.gerar_novos_dados, cursor="hand2"
        )
        self.btn_embaralhar.grid(row=0, column=4, padx=4)

        # Slider de Velocidade (delay em ms - limite até 300ms)
        lbl_vel = tk.Label(painel_topo, text="Velocidade:", bg=COR_PAINEL, fg=COR_TEXTO, font=("Helvetica", 10))
        lbl_vel.grid(row=0, column=5, padx=(15, 4))

        self.slider_delay = tk.Scale(
            painel_topo, from_=5, to=300, orient=tk.HORIZONTAL,
            bg=COR_PAINEL, fg=COR_TEXTO, highlightthickness=0,
            troughcolor="#313244", length=110, showvalue=False,
            command=self._ao_mudar_velocidade
        )
        self.slider_delay.set(50)  # Padrão: 50ms
        self.slider_delay.grid(row=0, column=6, padx=(0, 4))

        self.lbl_vel_val = tk.Label(painel_topo, text="50ms", bg=COR_PAINEL, fg="#f9e2af", font=("Helvetica", 9, "bold"), width=5)
        self.lbl_vel_val.grid(row=0, column=7, padx=(0, 10))

        # Slider de Quantidade de Elementos
        lbl_tam = tk.Label(painel_topo, text="Tamanho:", bg=COR_PAINEL, fg=COR_TEXTO, font=("Helvetica", 10))
        lbl_tam.grid(row=0, column=8, padx=(0, 4))

        self.slider_tamanho = tk.Scale(
            painel_topo, from_=10, to=70, orient=tk.HORIZONTAL,
            bg=COR_PAINEL, fg=COR_TEXTO, highlightthickness=0,
            troughcolor="#313244", length=90, command=self._ao_mudar_tamanho
        )
        self.slider_tamanho.set(self.tamanho_vetor)
        self.slider_tamanho.grid(row=0, column=9, padx=(0, 5))

        # 2. Barra de Informações Teóricas e Métricas
        painel_info = tk.Frame(self.root, bg="#181825", padx=15, pady=8)
        painel_info.pack(side=tk.TOP, fill=tk.X)

        self.lbl_teoria = tk.Label(
            painel_info, text="", bg="#181825", fg="#f5c2e7",
            font=("Helvetica", 10, "italic")
        )
        self.lbl_teoria.pack(side=tk.TOP, anchor="w")

        self.lbl_status = tk.Label(
            painel_info, text="Status: Pronto para iniciar",
            bg="#181825", fg=COR_TEXTO, font=("Helvetica", 10, "bold")
        )
        self.lbl_status.pack(side=tk.TOP, anchor="w", pady=(3, 0))

        # 3. Canvas de Visualização das Barras
        self.canvas = tk.Canvas(self.root, bg=COR_FUNDO, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        self.canvas.bind("<Configure>", lambda e: self.redesenhar())

        # 4. Rodapé com Legenda Colorida
        painel_rodape = tk.Frame(self.root, bg=COR_PAINEL, padx=15, pady=6)
        painel_rodape.pack(side=tk.BOTTOM, fill=tk.X)

        legenda_itens = [
            ("■ Comparando", COR_COMPARA),
            ("■ Trocando / Deslocando", COR_TROCA),
            ("■ Pivô / Chave", COR_PIVO),
            ("■ Ordenado", COR_CONCLUIDO),
            ("■ Aguardando", COR_BARRA_PADRAO),
        ]
        for texto, cor in legenda_itens:
            lbl = tk.Label(painel_rodape, text=texto, bg=COR_PAINEL, fg=cor, font=("Helvetica", 9, "bold"))
            lbl.pack(side=tk.LEFT, padx=10)

        self._ao_mudar_algoritmo()

    def _ao_mudar_algoritmo(self, event=None):
        alg = self.combo_algoritmo.get()
        info = INFOS_ALGORITMOS.get(alg, {})
        self.lbl_teoria.config(text=f"📌 {alg}: {info.get('complexidade', '')} | {info.get('resumo', '')}")
        self.parar_execucao()

    def _ao_mudar_velocidade(self, val):
        self.lbl_vel_val.config(text=f"{int(float(val))}ms")

    def _ao_mudar_tamanho(self, val):
        if not self.em_execucao:
            self.tamanho_vetor = int(val)
            self.gerar_novos_dados()

    def gerar_novos_dados(self):
        self.parar_execucao()
        self.dados = [random.randint(10, 100) for _ in range(self.tamanho_vetor)]
        self.lbl_status.config(text=f"Vetor gerado com {len(self.dados)} elementos. Clique em ▶ Iniciar.")
        self.redesenhar()

    def parar_execucao(self):
        if self.job_after:
            self.root.after_cancel(self.job_after)
            self.job_after = None
        self.em_execucao = False
        self.pausado = False
        self.gerador = None
        self.btn_iniciar.config(text="▶ Iniciar", bg="#a6e3a1")

    def alternar_iniciar_pausa(self):
        if not self.em_execucao:
            # Iniciar nova execução
            alg_nome = self.combo_algoritmo.get()
            alg_func = INFOS_ALGORITMOS[alg_nome]["func"]
            self.gerador = alg_func(self.dados.copy())
            self.em_execucao = True
            self.pausado = False
            self.btn_iniciar.config(text="⏸ Pausar", bg="#fab387")
            self._executar_loop()
        else:
            if self.pausado:
                # Retomar
                self.pausado = False
                self.btn_iniciar.config(text="⏸ Pausar", bg="#fab387")
                self._executar_loop()
            else:
                # Pausar
                self.pausado = True
                self.btn_iniciar.config(text="▶ Continuar", bg="#a6e3a1")
                if self.job_after:
                    self.root.after_cancel(self.job_after)
                    self.job_after = None

    def avancar_passo_unico(self):
        if not self.em_execucao:
            alg_nome = self.combo_algoritmo.get()
            alg_func = INFOS_ALGORITMOS[alg_nome]["func"]
            self.gerador = alg_func(self.dados.copy())
            self.em_execucao = True
            self.pausado = True
            self.btn_iniciar.config(text="▶ Continuar", bg="#a6e3a1")

        self._executar_um_passo()

    def _executar_loop(self):
        if self.pausado or not self.em_execucao:
            return

        concluiu = self._executar_um_passo()
        if not concluiu and self.em_execucao and not self.pausado:
            # Velocidade invertida: valor menor na escala = delay menor
            delay = int(self.slider_delay.get())
            self.job_after = self.root.after(delay, self._executar_loop)

    def _executar_um_passo(self) -> bool:
        """Executa um passo do gerador e atualiza a tela. Retorna True se terminou."""
        if not self.gerador:
            return True

        try:
            estado, destaques, tipo_acao, desc, comps, trocas = next(self.gerador)
            self.dados = estado
            self.lbl_status.config(
                text=f"Ação: {desc} | Comparações: {comps} | Trocas/Movimentos: {trocas}"
            )
            self.redesenhar(destaques=destaques, tipo_acao=tipo_acao)

            if tipo_acao == "done":
                self.parar_execucao()
                self.lbl_status.config(
                    text=f"✔ Concluído! Comparações: {comps} | Trocas/Movimentos: {trocas}"
                )
                return True
            return False
        except StopIteration:
            self.parar_execucao()
            return True

    def redesenhar(self, destaques=None, tipo_acao=""):
        if destaques is None:
            destaques = []

        self.canvas.delete("all")
        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()

        if largura <= 1 or altura <= 1 or not self.dados:
            return

        n = len(self.dados)
        max_val = max(self.dados) if max(self.dados) > 0 else 1
        espacamento = 4
        largura_barra = max(2, (largura - (n + 1) * espacamento) / n)

        for i, val in enumerate(self.dados):
            x0 = espacamento + i * (largura_barra + espacamento)
            x1 = x0 + largura_barra

            altura_barra = (val / max_val) * (altura - 45)
            y0 = altura - altura_barra - 20
            y1 = altura - 20

            # Determina cor da barra
            if i in destaques:
                if tipo_acao == "compare":
                    cor = COR_COMPARA
                elif tipo_acao in ("swap", "insert"):
                    cor = COR_TROCA
                elif tipo_acao == "pivot":
                    cor = COR_PIVO
                elif tipo_acao == "done":
                    cor = COR_CONCLUIDO
                else:
                    cor = COR_COMPARA
            else:
                cor = COR_BARRA_PADRAO

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=cor, outline="")

            # Mostra o valor no topo da barra se houver espaço
            if largura_barra >= 16:
                self.canvas.create_text(
                    (x0 + x1) / 2, y0 - 8,
                    text=str(val), fill=COR_TEXTO_MUTED, font=("Helvetica", 8)
                )


def main():
    root = tk.Tk()
    app = VisualizadorOrdenacaoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

