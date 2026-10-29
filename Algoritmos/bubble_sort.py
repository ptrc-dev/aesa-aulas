"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: BUBBLE SORT (ORDENAÇÃO POR FLUTUAÇÃO / BOLHA)
=============================================================================

Conceito:
---------
O Bubble Sort é o algoritmo de ordenação mais elementar e didático.
Seu nome vem da analogia física: os maiores elementos "flutuam" como bolhas
de ar para o topo (fim do vetor) a cada passagem:
1. Compara pares de elementos adjacentes (lado a lado): `arr[j]` e `arr[j+1]`.
2. Se estiverem fora de ordem (`arr[j] > arr[j+1]`), troca-os de lugar.
3. Ao fim da primeira passagem, o MAIOR elemento do vetor com certeza estará
   na última posição.
4. Repete o processo para os `n - 1` elementos restantes.
5. Com a otimização da flag `swapped`, se nenhuma troca ocorrer em uma passagem
   completa, o algoritmo detecta que a lista já está ordenada e encerra imediatamente.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n)       (com verificação da flag de troca em lista já ordenada)
- Caso Médio:     O(n^2)     (comparações e trocas quadráticas)
- Pior Caso:      O(n^2)     (quando a lista está em ordem decrescente)
- Espaço Auxiliar: O(1)       (in-place: ordena diretamente na memória)
- Estabilidade:   Estável    (preserva a ordem relativa de elementos com mesmo valor)
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista usando Bubble Sort com otimização de parada antecipada.
    
    :param arr: Lista de inteiros desordenada
    :return: Nova lista ordenada (cópia)
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    for i in range(n):
        houve_troca = False

        # Os últimos 'i' elementos já estão fixados na posição correta
        for j in range(0, n - i - 1):
            if arr_copia[j] > arr_copia[j + 1]:
                arr_copia[j], arr_copia[j + 1] = arr_copia[j + 1], arr_copia[j]
                houve_troca = True

        # Se nenhuma troca ocorreu nesta passagem, encerra mais cedo: O(n)
        if not houve_troca:
            break

    return arr_copia


def bubble_sort_in_place(arr: List[int]) -> None:
    """
    Versão in-place tradicional que modifica a lista passada diretamente.
    """
    n = len(arr)
    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                houve_troca = True
        if not houve_troca:
            break


def bubble_sort_didatico(arr: List[int]) -> List[int]:
    """
    Versão com explicações didáticas passo a passo de cada comparação e flutuação.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    print(f"Estado inicial do vetor: {arr_copia}\n")

    for i in range(n):
        houve_troca = False
        print(f"--- Passada {i + 1} (Buscando o maior elemento restante) ---")

        for j in range(0, n - i - 1):
            if arr_copia[j] > arr_copia[j + 1]:
                arr_copia[j], arr_copia[j + 1] = arr_copia[j + 1], arr_copia[j]
                houve_troca = True
                print(f"  Troca: arr[{j}]={arr_copia[j+1]} com arr[{j+1}]={arr_copia[j]} -> {arr_copia}")
            else:
                print(f"  Mantém: arr[{j}]={arr_copia[j]} <= arr[{j+1}]={arr_copia[j+1]}")

        print(f"Fim da passada {i + 1}: Maior elemento flutuou para o índice {n - i - 1} ({arr_copia[n - i - 1]})\n")

        if not houve_troca:
            print(">> Nenhuma troca detectada nesta passada! O vetor já está perfeitamente ordenado.")
            break

    return arr_copia


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DIDÁTICA DO BUBBLE SORT")
    print("=" * 65)

    # Exemplo 1: Visualização passo a passo detalhada
    amostra = [64, 34, 25, 12, 22]
    resultado = bubble_sort_didatico(amostra)
    print(f"Resultado Final Ordenado: {resultado}")

    # Exemplo 2: Testes em diferentes cenários
    cenarios = {
        "Vetor Aleatório": [5, 1, 4, 2, 8],
        "Vetor Já Ordenado (Melhor Caso - 1 passada O(n))": [1, 2, 3, 4, 5],
        "Vetor Invertido (Pior Caso O(n²))": [9, 7, 5, 3, 1],
        "Elementos Duplicados": [4, 2, 4, 1, 4, 3],
        "Vetor com Negativos": [-3, 10, -15, 0, 8, -1],
    }

    print("\n" + "=" * 65)
    print("TESTE EM DIFERENTES CENÁRIOS:")
    print("=" * 65)
    for nome, dados in cenarios.items():
        ordenado = bubble_sort(dados)
        print(f"[{nome}]")
        print(f"  Entrada : {dados}")
        print(f"  Saída   : {ordenado}\n")

