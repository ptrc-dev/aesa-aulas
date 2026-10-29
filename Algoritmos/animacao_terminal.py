"""
=============================================================================
ANIMADOR DE ALGORITMOS DE ORDENAÇÃO NO TERMINAL (ANSI ART)
=============================================================================

Este script renderiza uma animação em tempo real diretamente no terminal,
sem precisar de bibliotecas externas (usa apenas a biblioteca padrão do Python).

Recursos:
- Gráficos de barras horizontais com código de cores ANSI:
    * AMARELO : Elementos sendo comparados
    * VERMELHO: Elementos sendo trocados / deslocados
    * MAGENTA : Elemento pivô ou chave de inserção
    * VERDE   : Elementos ordenados / concluídos
    * CIANO   : Elementos normais em espera
- Estatísticas ao vivo: total de comparações, trocas e passo atual.
- Funciona em qualquer terminal moderno (macOS, Linux, VS Code, Windows Terminal).

Como executar:
    python3 Algoritmos/animacao_terminal.py
    python3 Algoritmos/animacao_terminal.py --demo (executa todos automaticamente)
"""

import os
import sys
import time
import random
from typing import List, Generator, Tuple, Dict, Any

# Códigos de Cores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
CLEAR_SCREEN = "\033[H\033[J"


# =============================================================================
# GERADORES DE PASSO A PASSO (ALGORITMOS COM YIELD)
# Cada gerador emite: (vetor_atual, indices_em_destaque, tipo_acao, descricao)
# =============================================================================

def anim_bubble_sort(arr: List[int]) -> Generator:
    n = len(arr)
    comp_count, swap_count = 0, 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comp_count += 1
            yield arr, [j, j + 1], "compare", f"Comparando arr[{j}]={arr[j]} e arr[{j+1}]={arr[j+1]}", comp_count, swap_count
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
                yield arr, [j, j + 1], "swap", f"Trocando {arr[j+1]} com {arr[j]}", comp_count, swap_count
        if not swapped:
            break
    yield arr, list(range(n)), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


def anim_insertion_sort(arr: List[int]) -> Generator:
    n = len(arr)
    comp_count, swap_count = 0, 0
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        yield arr, [i], "pivot", f"Chave selecionada para inserção: {chave}", comp_count, swap_count
        while j >= 0:
            comp_count += 1
            yield arr, [j, j + 1], "compare", f"Comparando chave {chave} com arr[{j}]={arr[j]}", comp_count, swap_count
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                swap_count += 1
                yield arr, [j, j + 1], "swap", f"Deslocando {arr[j]} para a direita", comp_count, swap_count
                j -= 1
            else:
                break
        arr[j + 1] = chave
        yield arr, [j + 1], "insert", f"Chave {chave} inserida na posição [{j + 1}]", comp_count, swap_count
    yield arr, list(range(n)), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


def anim_selection_sort(arr: List[int]) -> Generator:
    n = len(arr)
    comp_count, swap_count = 0, 0
    for i in range(n - 1):
        idx_menor = i
        yield arr, [i], "pivot", f"Procurando o menor elemento a partir de [{i}]", comp_count, swap_count
        for j in range(i + 1, n):
            comp_count += 1
            yield arr, [j, idx_menor], "compare", f"Comparando arr[{j}]={arr[j]} com menor atual arr[{idx_menor}]={arr[idx_menor]}", comp_count, swap_count
            if arr[j] < arr[idx_menor]:
                idx_menor = j
                yield arr, [idx_menor], "pivot", f"Novo menor encontrado: {arr[idx_menor]} no índice [{idx_menor}]", comp_count, swap_count
        if idx_menor != i:
            arr[i], arr[idx_menor] = arr[idx_menor], arr[i]
            swap_count += 1
            yield arr, [i, idx_menor], "swap", f"Trocando menor {arr[i]} para posição [{i}]", comp_count, swap_count
    yield arr, list(range(n)), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


def anim_quick_sort(arr: List[int]) -> Generator:
    comp_count = 0
    swap_count = 0

    def _quick(inicio: int, fim: int):
        nonlocal comp_count, swap_count
        if inicio < fim:
            pivo = arr[fim]
            yield arr, [fim], "pivot", f"Pivô escolhido: arr[{fim}]={pivo}", comp_count, swap_count
            i = inicio - 1
            for j in range(inicio, fim):
                comp_count += 1
                yield arr, [j, fim], "compare", f"Comparando arr[{j}]={arr[j]} com pivô {pivo}", comp_count, swap_count
                if arr[j] <= pivo:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    swap_count += 1
                    yield arr, [i, j], "swap", f"Trocando arr[{i}] e arr[{j}] na partição", comp_count, swap_count
            arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
            swap_count += 1
            p_index = i + 1
            yield arr, [p_index], "insert", f"Pivô {pivo} alocado no índice final [{p_index}]", comp_count, swap_count

            yield from _quick(inicio, p_index - 1)
            yield from _quick(p_index + 1, fim)

    yield from _quick(0, len(arr) - 1)
    yield arr, list(range(len(arr))), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


def anim_merge_sort(arr: List[int]) -> Generator:
    comp_count = 0
    swap_count = 0

    def _merge_sort(start: int, end: int):
        nonlocal comp_count, swap_count
        if end - start <= 1:
            return

        mid = (start + end) // 2
        yield from _merge_sort(start, mid)
        yield from _merge_sort(mid, end)

        left = arr[start:mid]
        right = arr[mid:end]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            comp_count += 1
            yield arr, [k, mid + j], "compare", f"Intercalando: comparando {left[i]} e {right[j]}", comp_count, swap_count
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            swap_count += 1
            yield arr, [k], "insert", f"Gravando {arr[k]} na posição ordenada [{k}]", comp_count, swap_count
            k += 1

        while i < len(left):
            arr[k] = left[i]
            swap_count += 1
            yield arr, [k], "insert", f"Inserindo restante da esquerda {left[i]} em [{k}]", comp_count, swap_count
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            swap_count += 1
            yield arr, [k], "insert", f"Inserindo restante da direita {right[j]} em [{k}]", comp_count, swap_count
            j += 1
            k += 1

    yield from _merge_sort(0, len(arr))
    yield arr, list(range(len(arr))), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


def anim_heap_sort(arr: List[int]) -> Generator:
    n = len(arr)
    comp_count = 0
    swap_count = 0

    def _heapify(tamanho: int, i: int):
        nonlocal comp_count, swap_count
        maior = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < tamanho:
            comp_count += 1
            yield arr, [esq, maior], "compare", f"Heap: Comparando filho esquerdo {arr[esq]} com {arr[maior]}", comp_count, swap_count
            if arr[esq] > arr[maior]:
                maior = esq

        if dir < tamanho:
            comp_count += 1
            yield arr, [dir, maior], "compare", f"Heap: Comparando filho direito {arr[dir]} com {arr[maior]}", comp_count, swap_count
            if arr[dir] > arr[maior]:
                maior = dir

        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            swap_count += 1
            yield arr, [i, maior], "swap", f"Heapify: Descendo elemento menor ({arr[i]} <-> {arr[maior]})", comp_count, swap_count
            yield from _heapify(tamanho, maior)

    # 1. Constrói o Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        yield from _heapify(n, i)

    yield arr, [0], "pivot", f"Max-Heap construído! Maior elemento está na raiz: {arr[0]}", comp_count, swap_count

    # 2. Extração
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swap_count += 1
        yield arr, [0, i], "swap", f"Extraindo maior valor {arr[i]} para a posição final [{i}]", comp_count, swap_count
        yield from _heapify(i, 0)

    yield arr, list(range(n)), "done", "Vetor 100% Ordenado com Sucesso!", comp_count, swap_count


# =============================================================================
# RENDERIZADOR ANSI NO TERMINAL
# =============================================================================

def desenhar_quadro(nome_algoritmo: str, arr: List[int], destaques: List[int],
                   tipo_acao: str, descricao: str, comps: int, trocas: int, delay: float):
    """
    Limpa a tela e renderiza o estado atual das barras no terminal.
    """
    buffer = []
    buffer.append(CLEAR_SCREEN)
    buffer.append(f"{BOLD}{WHITE}==================================================================={RESET}")
    buffer.append(f"{BOLD}🎬 SIMULADOR VISUAL DE ORDENAÇÃO: {CYAN}{nome_algoritmo.upper()}{RESET}")
    buffer.append(f"{BOLD}{WHITE}==================================================================={RESET}")
    buffer.append(f"Passo: {WHITE}{descricao}{RESET}")
    buffer.append(f"Métricas: Comparações: {YELLOW}{comps}{RESET} | Trocas/Movimentos: {RED}{trocas}{RESET}\n")

    # Legenda
    buffer.append(f"Legenda: {YELLOW}■ Comparando{RESET} | {RED}■ Trocando/Movendo{RESET} | {MAGENTA}■ Pivô/Chave{RESET} | {GREEN}■ Concluído{RESET} | {CYAN}■ Aguardando{RESET}\n")

    max_val = max(arr) if arr else 1
    largura_maxima = 40  # Largura máxima em caracteres de bloco

    # Desenho de cada barra horizontal
    for idx, val in enumerate(arr):
        tamanho_barra = int((val / max_val) * largura_maxima)
        tamanho_barra = max(1, tamanho_barra)

        # Escolhe a cor baseada na ação
        if idx in destaques:
            if tipo_acao == "compare":
                cor = YELLOW
                simbolo = "◄ (Comparando)"
            elif tipo_acao == "swap":
                cor = RED
                simbolo = "◄ (Trocando)"
            elif tipo_acao in ("pivot", "insert"):
                cor = MAGENTA
                simbolo = "◄ (Pivô / Chave)"
            elif tipo_acao == "done":
                cor = GREEN
                simbolo = "✔"
            else:
                cor = YELLOW
                simbolo = "◄"
        else:
            cor = CYAN
            simbolo = ""

        barra = "█" * tamanho_barra
        buffer.append(f"{idx:02d} | {val:03d} | {cor}{barra}{RESET} {cor}{simbolo}{RESET}")

    buffer.append(f"\n{BOLD}{WHITE}==================================================================={RESET}")
    sys.stdout.write("\n".join(buffer) + "\n")
    sys.stdout.flush()
    time.sleep(delay)


def executar_animacao(nome: str, funcao_gerador, dados: List[int], delay: float = 0.08):
    """
    Executa a animação para um determinado algoritmo.
    """
    copia = dados.copy()
    for estado, destaques, tipo, desc, comps, trocas in funcao_gerador(copia):
        desenhar_quadro(nome, estado, destaques, tipo, desc, comps, trocas, delay)
    time.sleep(0.5)


# =============================================================================
# MENU PRINCIPAL / CLI
# =============================================================================

ALGORITMOS = {
    "1": ("Bubble Sort", anim_bubble_sort),
    "2": ("Insertion Sort", anim_insertion_sort),
    "3": ("Selection Sort", anim_selection_sort),
    "4": ("Merge Sort", anim_merge_sort),
    "5": ("Quick Sort", anim_quick_sort),
    "6": ("Heap Sort", anim_heap_sort),
}


def main():
    # Modo de demonstração automática (para testes ou exibição rápida)
    if "--demo" in sys.argv:
        dados = [45, 12, 85, 32, 89, 39, 69, 44, 42, 1, 98, 20]
        for num, (nome, func) in ALGORITMOS.items():
            executar_animacao(nome, func, dados, delay=0.03)
            time.sleep(0.8)
        print("\nDemonstração concluída!")
        return

    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print(f"{BOLD}{CYAN}======================================================{RESET}")
        print(f"{BOLD}      ANIMADOR DIDÁTICO DE ORDENAÇÃO NO TERMINAL      {RESET}")
        print(f"{BOLD}{CYAN}======================================================{RESET}")
        print("Escolha o algoritmo que deseja animar:")
        print("  [1] Bubble Sort")
        print("  [2] Insertion Sort")
        print("  [3] Selection Sort")
        print("  [4] Merge Sort")
        print("  [5] Quick Sort")
        print("  [6] Heap Sort")
        print("  [7] Executar TODOS em Sequência (Demonstração Completa)")
        print("  [0] Sair")
        print("-" * 54)

        opcao = input(f"{BOLD}Digite a opção desejada: {RESET}").strip()

        if opcao == "0":
            print("\nEncerrando visualizador. Até a próxima aula!\n")
            break

        # Gera array aleatório para a demonstração
        tamanho = 14
        dados = random.sample(range(5, 99), tamanho)

        # Velocidade configurável
        delay = 0.08

        if opcao in ALGORITMOS:
            nome, func = ALGORITMOS[opcao]
            executar_animacao(nome, func, dados, delay=delay)
            input(f"\n{BOLD}Pressione [ENTER] para voltar ao menu...{RESET}")
        elif opcao == "7":
            for _, (nome, func) in ALGORITMOS.items():
                executar_animacao(nome, func, dados, delay=0.05)
                time.sleep(1.0)
            input(f"\n{BOLD}Todos concluídos! Pressione [ENTER] para voltar ao menu...{RESET}")
        else:
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")
            time.sleep(1.0)


if __name__ == "__main__":
    main()

