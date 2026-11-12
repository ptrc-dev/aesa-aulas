"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: SELECTION SORT (ORDENAÇÃO POR SELEÇÃO)
=============================================================================

Conceito:
---------
O Selection Sort baseia-se na ideia intuitiva de encontrar iterativamente
o menor elemento e colocá-lo na posição correta:
1. Divide mentalmente o array em duas regiões:
   - Uma sublista à esquerda, que já está ordenada (inicia vazia).
   - Uma sublista à direita, que ainda não está ordenada (inicia com todo o vetor).
2. Na primeira iteração, busca o MENOR elemento de todo o vetor e o troca
   com o elemento da posição 0.
3. Na segunda iteração, busca o menor elemento a partir da posição 1 e o troca
   com a posição 1.
4. Repete o processo até que a fronteira atinja o penúltimo elemento.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n^2)  (mesmo com a lista ordenada, continua comparando para ter certeza)
- Caso Médio:     O(n^2)  (número fixo de comparações: n*(n-1)/2)
- Pior Caso:      O(n^2)  (mesmo número de comparações)
- Espaço Auxiliar: O(1)    (in-place: ordena diretamente no vetor)
- Trocas (Swaps): O(n)    (no máximo n - 1 trocas no total!)
- Estabilidade:   Não estável na versão in-place (uma troca longa pode alterar
                  a ordem relativa de chaves iguais)

Vantagem Prática Única do Selection Sort:
- **Número Mínimo de Escritas:** Enquanto Bubble Sort e Insertion Sort podem fazer
  até O(n^2) trocas/escritas de memória, o Selection Sort faz no máximo O(n) trocas.
- Isso o torna muito útil em sistemas embarcados onde a escrita em memórias
  Flash ou EEPROM possui custo elevado ou limite de ciclos de vida.
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista usando o algoritmo Selection Sort.
    
    :param arr: Lista de inteiros desordenada
    :return: Nova lista ordenada (cópia)
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    # Percorre o vetor até o penúltimo elemento
    for i in range(n - 1):
        # Assume inicialmente que o menor elemento está no índice 'i'
        indice_menor = i

        # Procura o menor elemento no restante não ordenado do vetor
        for j in range(i + 1, n):
            if arr_copia[j] < arr_copia[indice_menor]:
                indice_menor = j

        # Se encontrou um elemento menor, realiza a troca
        if indice_menor != i:
            arr_copia[i], arr_copia[indice_menor] = arr_copia[indice_menor], arr_copia[i]

    return arr_copia


def selection_sort_in_place(arr: List[int]) -> None:
    """
    Versão clássica in-place que modifica a lista diretamente na memória.
    """
    n = len(arr)
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]


def selection_sort_didatico(arr: List[int]) -> List[int]:
    """
    Versão didática que exibe passo a passo a localização do menor
    elemento e a troca pontual realizada.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)

    print(f"Estado inicial do vetor: {arr_copia}\n")

    for i in range(n - 1):
        indice_menor = i
        comparacoes = 0
        print(f"--- Passo {i + 1}: Procurando menor valor a partir do índice {i} ({arr_copia[i]}) ---")

        for j in range(i + 1, n):
            comparacoes += 1
            if arr_copia[j] < arr_copia[indice_menor]:
                print(f"  Novo menor encontrado: {arr_copia[j]} no índice {j} (superou {arr_copia[indice_menor]})")
                indice_menor = j

        if indice_menor != i:
            menor_val = arr_copia[indice_menor]
            arr_copia[i], arr_copia[indice_menor] = arr_copia[indice_menor], arr_copia[i]
            print(f"  >> Troca realizada: {menor_val} <-> {arr_copia[indice_menor]}")
        else:
            print(f"  >> Elemento {arr_copia[i]} já estava na posição correta (sem necessidade de troca)")

        print(f"  Vetor resultante do passo: {arr_copia}")
        print(f"  Parte já ordenada: {arr_copia[:i + 1]}\n")

    return arr_copia


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DIDÁTICA DO SELECTION SORT (SELEÇÃO)")
    print("=" * 65)

    # Exemplo 1: Visualização passo a passo detalhada
    amostra = [64, 25, 12, 22, 11]
    resultado = selection_sort_didatico(amostra)
    print(f"Resultado Final Ordenado: {resultado}")

    # Exemplo 2: Testes em diferentes cenários
    cenarios = {
        "Vetor Aleatório": [29, 10, 14, 37, 13],
        "Vetor Já Ordenado": [1, 2, 3, 4, 5],
        "Vetor Invertido": [50, 40, 30, 20, 10],
        "Elementos Duplicados": [7, 2, 7, 3, 2, 8, 1],
        "Vetor com Negativos": [-12, 0, 45, -3, 8, -30],
    }

    print("\n" + "=" * 65)
    print("TESTE EM DIFERENTES CENÁRIOS:")
    print("=" * 65)
    for nome, dados in cenarios.items():
        ordenado = selection_sort(dados)
        print(f"[{nome}]")
        print(f"  Entrada : {dados}")
        print(f"  Saída   : {ordenado}\n")

