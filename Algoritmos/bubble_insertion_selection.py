"""
=============================================================================
ALGORITMOS ELEMENTARES DE ORDENAÇÃO:
BUBBLE SORT, INSERTION SORT E SELECTION SORT
=============================================================================

Visão Geral:
------------
Esses três algoritmos formam a base dos estudos de ordenação na Ciência da Computação.
Possuem complexidade assintótica média de O(n^2), mas cada um possui características,
mecanismos e casos de uso específicos.

Tabela Comparativa:
------------------------------------------------------------------------------------------
Algoritmo        Melhor      Médio       Pior        Espaço   Trocas (Pior)   Estável?
------------------------------------------------------------------------------------------
Bubble Sort      O(n)        O(n^2)      O(n^2)      O(1)     O(n^2)          Sim
Insertion Sort   O(n)        O(n^2)      O(n^2)      O(1)     O(n^2)          Sim
Selection Sort   O(n^2)      O(n^2)      O(n^2)      O(1)     O(n)            Não*
------------------------------------------------------------------------------------------
* A versão padrão in-place do Selection Sort não é estável.

1. Bubble Sort (Ordenação por Flutuação/Bolha):
   - Percorre repetidamente a lista, comparando elementos adjacentes e trocando-os
     se estiverem fora de ordem.
   - Os elementos maiores "flutuam" para o fim da lista a cada passada.
   - Com uma flag booleana de verificação de trocas (`swapped`), encerra imediatamente
     se a lista já estiver ordenada (Melhor Caso: O(n)).

2. Insertion Sort (Ordenação por Inserção):
   - Semelhante à forma como organizamos cartas de baralho na mão: divide a lista em
     uma porção já ordenada (à esquerda) e uma porção desordenada (à direita).
   - Pega um elemento de cada vez e o insere na sua posição correta na parte ordenada,
     deslocando os elementos maiores para a direita.
   - É o algoritmo elementar mais eficiente na prática para listas pequenas ou listas
     quase ordenadas. Usado como base nos algoritmos híbridos Timsort (Python/Java)
     e Introsort (C++).

3. Selection Sort (Ordenação por Seleção):
   - Divide a lista em duas partes: ordenada e não ordenada.
   - A cada iteração, procura o MENOR elemento na porção não ordenada e o troca com
     o primeiro elemento dessa porção.
   - Característica fundamental: Faz no máximo O(n) trocas (writes). Isso o torna
     ideal em sistemas embarcados onde a escrita em memória (como Flash ou EEPROM)
     é uma operação de alto custo.
"""

from typing import List, Tuple, Dict


# =============================================================================
# 1. BUBBLE SORT
# =============================================================================
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista usando Bubble Sort com otimização de parada antecipada.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    for i in range(n):
        houve_troca = False
        # Os últimos 'i' elementos já estão em suas posições corretas
        for j in range(0, n - i - 1):
            if arr_copia[j] > arr_copia[j + 1]:
                arr_copia[j], arr_copia[j + 1] = arr_copia[j + 1], arr_copia[j]
                houve_troca = True

        # Se nenhuma troca ocorreu nesta passagem, a lista já está ordenada
        if not houve_troca:
            break

    return arr_copia


# =============================================================================
# 2. INSERTION SORT (INSERÇÃO)
# =============================================================================
def insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista inserindo cada elemento em sua posição correta
    na sublista já ordenada à sua esquerda.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    for i in range(1, n):
        chave = arr_copia[i]
        j = i - 1

        # Move os elementos da parte ordenada que são maiores que a chave
        # uma posição para a frente da sua posição atual
        while j >= 0 and arr_copia[j] > chave:
            arr_copia[j + 1] = arr_copia[j]
            j -= 1

        arr_copia[j + 1] = chave

    return arr_copia


# =============================================================================
# 3. SELECTION SORT (SELEÇÃO)
# =============================================================================
def selection_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista selecionando repetidamente o menor elemento
    da parte não ordenada e trocando-o para o início dessa parte.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    for i in range(n - 1):
        # Encontra o índice do menor elemento restante
        indice_menor = i
        for j in range(i + 1, n):
            if arr_copia[j] < arr_copia[indice_menor]:
                indice_menor = j

        # Realiza no máximo 1 troca por passagem externa
        if indice_menor != i:
            arr_copia[i], arr_copia[indice_menor] = arr_copia[indice_menor], arr_copia[i]

    return arr_copia


# =============================================================================
# VERSÃO DIDÁTICA: CONTADOR DE COMPARAÇÕES E TROCAS
# =============================================================================
def analisar_algoritmos(arr: List[int]) -> Dict[str, Dict[str, int]]:
    """
    Executa os três algoritmos registrando o número exato de comparações
    e trocas/atribuições realizadas em cada um.
    """
    resultados = {}

    # --- Análise do Bubble Sort ---
    copia_bubble = arr.copy()
    comp_bubble, trocas_bubble = 0, 0
    n = len(copia_bubble)
    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            comp_bubble += 1
            if copia_bubble[j] > copia_bubble[j + 1]:
                copia_bubble[j], copia_bubble[j + 1] = copia_bubble[j + 1], copia_bubble[j]
                trocas_bubble += 1
                houve_troca = True
        if not houve_troca:
            break
    resultados["Bubble Sort"] = {"comparacoes": comp_bubble, "trocas": trocas_bubble}

    # --- Análise do Insertion Sort ---
    copia_insert = arr.copy()
    comp_insert, deslocamentos_insert = 0, 0
    for i in range(1, len(copia_insert)):
        chave = copia_insert[i]
        j = i - 1
        while j >= 0:
            comp_insert += 1
            if copia_insert[j] > chave:
                copia_insert[j + 1] = copia_insert[j]
                deslocamentos_insert += 1
                j -= 1
            else:
                break
        copia_insert[j + 1] = chave
    resultados["Insertion Sort"] = {"comparacoes": comp_insert, "trocas": deslocamentos_insert}

    # --- Análise do Selection Sort ---
    copia_select = arr.copy()
    comp_select, trocas_select = 0, 0
    for i in range(len(copia_select) - 1):
        idx_menor = i
        for j in range(i + 1, len(copia_select)):
            comp_select += 1
            if copia_select[j] < copia_select[idx_menor]:
                idx_menor = j
        if idx_menor != i:
            copia_select[i], copia_select[idx_menor] = copia_select[idx_menor], copia_select[i]
            trocas_select += 1
    resultados["Selection Sort"] = {"comparacoes": comp_select, "trocas": trocas_select}

    return resultados


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("DEMONSTRAÇÃO: BUBBLE SORT, INSERTION SORT E SELECTION SORT")
    print("=" * 75)

    amostra = [29, 10, 14, 37, 13]
    print(f"\nArray Original: {amostra}\n")

    # Demonstração individual
    print("--- 1. Execução Individual dos Algoritmos ---")
    print(f"Bubble Sort    : {bubble_sort(amostra)}")
    print(f"Insertion Sort : {insertion_sort(amostra)}")
    print(f"Selection Sort : {selection_sort(amostra)}")

    # Demonstração comparativa de métricas em diferentes cenários
    print("\n" + "=" * 75)
    print("--- 2. Comparativo de Operações (Comparações vs Trocas/Movimentos) ---")
    print("=" * 75)

    cenarios = {
        "Vetor Aleatório [64, 25, 12, 22, 11]": [64, 25, 12, 22, 11],
        "Vetor Já Ordenado [10, 20, 30, 40, 50] (Melhor Caso)": [10, 20, 30, 40, 50],
        "Vetor Invertido [50, 40, 30, 20, 10] (Pior Caso)": [50, 40, 30, 20, 10],
    }

    for titulo, dados in cenarios.items():
        print(f"\n>>> Cenário: {titulo}")
        analise = analisar_algoritmos(dados)
        print(f"{'Algoritmo':<18} | {'Comparações':<12} | {'Trocas/Movimentos':<18}")
        print("-" * 55)
        for alg, metricas in analise.items():
            print(f"{alg:<18} | {metricas['comparacoes']:<12} | {metricas['trocas']:<18}")

