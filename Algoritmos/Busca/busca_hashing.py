"""
=============================================================================
ALGORITMO DE BUSCA: BUSCA POR HASHING (TABELA HASH / DISPERSÃO)
=============================================================================

Conceito:
---------
Diferente da Busca Linear e da Busca Binária — que encontram elementos através
de sucessivas comparações entre chaves —, o Hashing calcula DIRETAMENTE o endereço
de memória (índice) onde o dado reside ou deve ser armazenado.

Isso é feito aplicando uma "Função Hash" (Função de Espalhamento ou Dispersão)
sobre a chave de busca:

               Chave  ---> [ Função Hash ] ---> Índice no Array
              "Maria" --->  h("Maria")     ---> 4

Acesso Direto:
Uma vez calculado o índice, acessamos o elemento em tempo constante: O(1).

O Desafio das Colisões:
-----------------------
Como o conjunto de chaves possíveis é infinito (ou muito grande) e o tamanho
da tabela é finito, duas chaves distintas podem resultar no mesmo índice:
                h("Ana") == h("Carlos") == índice 2
Esse fenômeno é inevitável e chama-se COLISÃO.

Principais Métodos de Tratamento de Colisão:
1. Encadeamento Separado (Separate Chaining):
   Cada posição do vetor da tabela guarda uma lista (ou balde/bucket).
   Se houver colisão, o novo par (chave, valor) é simplesmente adicionado à lista
   daquela posição.
2. Endereçamento Aberto (Open Addressing) / Sondagem Linear:
   Todos os elementos residem diretamente no vetor da tabela. Se a posição
   calculada estiver ocupada, procura-se a próxima posição livre sequencialmente
   (índice + 1, índice + 2, ...).

Complexidade Assintótica:
-------------------------
- Busca / Inserção / Remoção:
  * Melhor Caso:    O(1)   (chave encontrada diretamente sem colisão)
  * Caso Médio:     O(1)   (função hash uniforme e fator de carga controlado)
  * Pior Caso:      O(n)   (caso patológico onde todas as chaves colidem no mesmo bucket)
- Espaço Auxiliar:  O(m + n), onde m é o tamanho da tabela e n é o total de elementos.

Fator de Carga (Load Factor - α):
---------------------------------
α = n / m  (número de elementos dividido pela capacidade da tabela).
Quando o fator de carga ultrapassa determinado limiar (ex: 0.75), a tabela
normalmente é redimensionada (Rehash) para manter as operações em O(1).

Vantagens:
----------
- Operações de busca e inserção quase instantâneas O(1).
- É a estrutura de dados base de dicionários em Python (`dict`), conjuntos (`set`),
  `HashMap` em Java e bancos NoSQL chave-valor (como Redis).

Desvantagens:
-------------
- Não preserva a ordem natural dos dados (não suporta buscas de intervalo de forma eficiente).
- Pode consumir mais memória para manter posições livres e evitar colisões.
- Requer uma boa função hash para espalhar uniformemente os dados.
"""

from typing import Any, List, Optional, Tuple


# =============================================================================
# 1. TABELA HASH COM ENCADEAMENTO SEPARADO (SEPARATE CHAINING)
# =============================================================================
class TabelaHashEncadeada:
    """
    Implementação de Tabela Hash didática utilizando Encadeamento Separado
    para resolver colisões (cada bucket é uma lista de tuplas [chave, valor]).
    """

    def __init__(self, capacidade: int = 7):
        """
        Inicializa a tabela com capacidade fixa (usar número primo reduz colisões).
        """
        self.capacidade = capacidade
        # Cada bucket é uma lista dinâmica independente
        self.tabela: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacidade)]
        self.total_itens = 0

    def _funcao_hash(self, chave: Any) -> int:
        """
        Função de dispersão (hash) didática:
        - Para inteiros: método da divisão (chave % capacidade).
        - Para strings ou outros tipos: soma dos códigos ASCII dos caracteres.
        """
        if isinstance(chave, int):
            hash_valor = chave
        else:
            # Algoritmo polinomial clássico para strings (estilo Java hashCode)
            hash_valor = 0
            for char in str(chave):
                hash_valor = (hash_valor * 31 + ord(char))

        return hash_valor % self.capacidade

    def inserir(self, chave: Any, valor: Any) -> None:
        """
        Insere ou atualiza o par (chave, valor) na tabela.
        Tempo médio: O(1).
        """
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        # Verifica se a chave já existe para atualizar o valor
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)
                return

        # Se não existe, adiciona ao bucket (trata a colisão encadeando)
        bucket.append((chave, valor))
        self.total_itens += 1

    def buscar(self, chave: Any) -> Optional[Any]:
        """
        Busca o valor associado a uma chave calculando seu hash diretamente.
        Tempo médio: O(1). Retorna None se a chave não existir.
        """
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        for k, v in bucket:
            if k == chave:
                return v

        return None

    def remover(self, chave: Any) -> bool:
        """
        Remove um par chave-valor da tabela.
        Retorna True se removeu com sucesso, ou False se não existia.
        """
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        for i, (k, v) in enumerate(bucket):
            if k == chave:
                del bucket[i]
                self.total_itens -= 1
                return True

        return False

    def fator_de_carga(self) -> float:
        """Retorna o fator de carga atual (α = n / m)."""
        return self.total_itens / self.capacidade

    def exibir_estrutura(self) -> None:
        """Exibe o mapa de buckets da tabela e as colisões no terminal."""
        print(f"\n--- Estrutura Interna da Tabela Hash (Capacidade: {self.capacidade}, Itens: {self.total_itens}, Carga: {self.fator_de_carga():.2f}) ---")
        for indice, bucket in enumerate(self.tabela):
            if not bucket:
                conteudo = "[ VAZIO ]"
            else:
                conteudo = " -> ".join([f"({k}: '{v}')" for k, v in bucket])
            print(f"Bucket [{indice:02d}]: {conteudo}")
        print("-" * 65)


# =============================================================================
# 2. TABELA HASH COM ENDEREÇAMENTO ABERTO (SONDAGEM LINEAR)
# =============================================================================
class TabelaHashSondagemLinear:
    """
    Implementação com Endereçamento Aberto:
    Todos os elementos ficam no mesmo vetor.
    Se o índice calculado estiver ocupado, testa o índice (pos + 1) % capacidade.
    """

    def __init__(self, capacidade: int = 11):
        self.capacidade = capacidade
        self.chaves: List[Optional[Any]] = [None] * capacidade
        self.valores: List[Optional[Any]] = [None] * capacidade
        self.total_itens = 0
        self._DELETADO = object()  # Marcador especial (tombstone) para itens removidos

    def _funcao_hash(self, chave: Any) -> int:
        if isinstance(chave, int):
            return chave % self.capacidade
        return sum(ord(c) for c in str(chave)) % self.capacidade

    def inserir(self, chave: Any, valor: Any) -> bool:
        if self.total_itens >= self.capacidade:
            print("Erro: Tabela Hash cheia!")
            return False

        pos = self._funcao_hash(chave)

        # Sondagem linear: procura a próxima posição livre ou a mesma chave
        while self.chaves[pos] is not None and self.chaves[pos] is not self._DELETADO:
            if self.chaves[pos] == chave:
                self.valores[pos] = valor  # Atualização
                return True
            pos = (pos + 1) % self.capacidade

        self.chaves[pos] = chave
        self.valores[pos] = valor
        self.total_itens += 1
        return True

    def buscar(self, chave: Any) -> Optional[Any]:
        pos = self._funcao_hash(chave)
        inicio = pos

        while self.chaves[pos] is not None:
            if self.chaves[pos] == chave:
                return self.valores[pos]
            pos = (pos + 1) % self.capacidade
            if pos == inicio:
                break  # Deu uma volta completa

        return None

    def exibir_estrutura(self) -> None:
        print(f"\n--- Estrutura (Sondagem Linear - Capacidade: {self.capacidade}) ---")
        for i in range(self.capacidade):
            k = self.chaves[i]
            v = self.valores[i]
            if k is None:
                estado = "[ VAZIO ]"
            elif k is self._DELETADO:
                estado = "[ REMOVIDO ]"
            else:
                estado = f"Chave: {k} | Valor: '{v}'"
            print(f"Slot [{i:02d}]: {estado}")
        print("-" * 65)


# =============================================================================
# DEMONSTRAÇÕES E CASOS DE TESTE
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DO ALGORITMO DE BUSCA POR HASHING (TABELA HASH)")
    print("=" * 65)

    # 1. Demonstração com Encadeamento Separado
    print("\n1. CRIANDO TABELA HASH COM ENCADEAMENTO (Capacidade = 7):")
    th = TabelaHashEncadeada(capacidade=7)

    # Inserção de dados
    dados_alunos = [
        ("202301", "Ana Silva"),
        ("202302", "Bruno Costa"),
        ("202308", "Carlos Eduardo"),  # Irá colidir propositalmente dependendo do hash
        ("202315", "Daniela Souza"),
        ("202322", "Eduardo Pereira"),
    ]

    print("\nInserindo alunos na tabela:")
    for matricula, nome in dados_alunos:
        h = th._funcao_hash(matricula)
        print(f"  Chave: '{matricula}' -> Hash calculado = {h} -> Guardado no Bucket [{h}]")
        th.inserir(matricula, nome)

    # Exibe como a tabela organiza colisões em buckets
    th.exibir_estrutura()

    # 2. Demonstração da Busca O(1)
    print("2. REALIZANDO BUSCAS POR CHAVE (TEMPO O(1)):")
    chaves_busca = ["202301", "202308", "999999"]

    for chave in chaves_busca:
        h = th._funcao_hash(chave)
        resultado = th.buscar(chave)
        if resultado:
            print(f"-> Busca Chave '{chave}': Acessou Bucket [{h}] -> Aluno Encontrado: '{resultado}'")
        else:
            print(f"-> Busca Chave '{chave}': Acessou Bucket [{h}] -> Matrícula NÃO encontrada.")

    # 3. Teste de Remoção
    print("\n3. REMOVENDO UMA CHAVE:")
    removido = th.remover("202308")
    print(f"Remover chave '202308': {'Sucesso' if removido else 'Falha'}")
    th.exibir_estrutura()

    # 4. Demonstração de Sondagem Linear (Endereçamento Aberto)
    print("\n4. TESTE DE ENDEREÇAMENTO ABERTO COM SONDAGEM LINEAR:")
    th_linear = TabelaHashSondagemLinear(capacidade=5)
    # Inserções propositais para forçar colisões
    th_linear.inserir(10, "Carro")   # 10 % 5 = 0
    th_linear.inserir(15, "Moto")    # 15 % 5 = 0 (COLISÃO! vai para slot 1)
    th_linear.inserir(20, "Barco")   # 20 % 5 = 0 (COLISÃO! vai para slot 2)
    th_linear.inserir(12, "Avião")   # 12 % 5 = 2 (COLISÃO! slot 2 ocupado, vai para slot 3)

    th_linear.exibir_estrutura()

    print(f"Busca chave 15: '{th_linear.buscar(15)}' (encontrado no slot com sondagem)")
    print(f"Busca chave 99: {th_linear.buscar(99)} (não existente)")

