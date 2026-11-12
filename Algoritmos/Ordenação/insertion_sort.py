"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: INSERTION SORT (ORDENAÇÃO POR INSERÇÃO)
=============================================================================

Conceito:
---------
O Insertion Sort é um algoritmo simples e intuitivo. Seu funcionamento é idêntico
à maneira como a maioria das pessoas organiza cartas de baralho na mão:
1. Considera-se que o primeiro elemento já está ordenado (sublista de tamanho 1).
2. Pega-se o próximo elemento (a "chave") da parte não ordenada.
3. Compara-se a chave com os elementos da parte ordenada, da direita para a esquerda.
4. Deslocam-se todos os elementos maiores que a chave uma posição para a direita.
5. Insere-se a chave no espaço que sobrou.
6. Repete-se até o final do vetor.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n)       (quando o array já está ordenado ou quase ordenado)
- Caso Médio:     O(n^2)     (comparações e deslocamentos quadráticos)
- Pior Caso:      O(n^2)     (quando o array está em ordem decrescente)
- Espaço Auxiliar: O(1)       (in-place: não requer memória adicional)
- Estabilidade:   Estável    (preserva a ordem relativa de elementos iguais)

Por que o Insertion Sort é importante na prática?
- É o algoritmo mais rápido para listas pequenas (tipicamente N <= 30 a 50 elementos).
- É adaptativo: se os dados já estiverem quase ordenados, roda em tempo linear O(n).
- É a base do **Timsort** (o algoritmo de ordenação nativo do Python `sort()` e do Java)
  e do **Introsort** (usado no `std::sort` do C++).
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista usando o algoritmo Insertion Sort.
    
    :param arr: Lista de inteiros desordenada
    :return: Nova lista ordenada (cópia)
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    # Percorre do segundo elemento (índice 1) até o final
    for i in range(1, n):
        chave = arr_copia[i]
        j = i - 1

        # Desloca elementos maiores que a chave para a direita
        while j >= 0 and arr_copia[j] > chave:
            arr_copia[j + 1] = arr_copia[j]
            j -= 1

        # Insere a chave na sua posição correta
        arr_copia[j + 1] = chave

    return arr_copia


def insertion_sort_in_place(arr: List[int]) -> None:
    """
    Versão clássica in-place que modifica a lista diretamente na memória.
    """
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave


def insertion_sort_didatico(arr: List[int]) -> List[int]:
    """
    Versão com exibição pedagógica passo a passo dos deslocamentos e inserções.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    print(f"Estado inicial do vetor: {arr_copia}")
    print("Parte ordenada inicial: [", arr_copia[0], "]\n")

    for i in range(1, n):
        chave = arr_copia[i]
        j = i - 1
        deslocamentos = 0

        print(f"--- Passo {i}: Inserindo chave [{chave}] ---")
        print(f"  Vetor antes do passo: {arr_copia}")

        while j >= 0 and arr_copia[j] > chave:
            arr_copia[j + 1] = arr_copia[j]
            deslocamentos += 1
            print(f"    Deslocou {arr_copia[j]} para a direita -> {arr_copia}")
            j -= 1

        arr_copia[j + 1] = chave
        print(f"  >> Chave {chave} inserida na posição {j + 1} (Total deslocamentos: {deslocamentos})")
        print(f"  Sublista ordenada até agora: {arr_copia[:i + 1]}\n")

    return arr_copia


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DIDÁTICA DO INSERTION SORT (INSERÇÃO)")
    print("=" * 65)

    # Exemplo 1: Visualização passo a passo detalhada
    amostra = [12, 11, 13, 5, 6]
    resultado = insertion_sort_didatico(amostra)
    print(f"Resultado Final Ordenado: {resultado}")

    # Exemplo 2: Testes em diferentes cenários
    cenarios = {
        "Vetor Aleatório": [64, 34, 25, 12, 22, 11, 90],
        "Vetor Já Ordenado (Melhor Caso O(n))": [10, 20, 30, 40, 50, 60],
        "Vetor Invertido (Pior Caso O(n²))": [90, 70, 50, 30, 10],
        "Elementos Duplicados": [8, 3, 5, 3, 1, 8, 2],
        "Vetor com Negativos": [-4, 15, -20, 0, 7, -2],
    }

    print("\n" + "=" * 65)
    print("TESTE EM DIFERENTES CENÁRIOS:")
    print("=" * 65)
    for nome, dados in cenarios.items():
        ordenado = insertion_sort(dados)
        print(f"[{nome}]")
        print(f"  Entrada : {dados}")
        print(f"  Saída   : {ordenado}\n")

