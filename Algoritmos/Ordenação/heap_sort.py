"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: HEAP SORT (ORDENAÇÃO POR HEAP BINÁRIO)
=============================================================================

Conceito:
---------
Criado por J. W. J. Williams em 1964, o Heap Sort utiliza uma estrutura de dados
chamada Heap Binário (Binary Heap) para ordenar os elementos.

O Heap Binário é uma Árvore Binária Quase Completa mapeada diretamente em um
array sequencial, sem necessidade de ponteiros:
- Para qualquer nó no índice `i`:
    - Filho da esquerda : 2 * i + 1
    - Filho da direita  : 2 * i + 2
    - Nó Pai            : (i - 1) // 2

Propriedade do Max-Heap:
- O valor de cada nó pai é SEMPRE maior ou igual ao valor de seus filhos.
- Consequentemente, o MAIOR elemento do conjunto está sempre na RAIZ (índice 0).

Fases do Heap Sort:
1. Construção do Max-Heap (Build Heap): Transforma o array arbitrário em um Max-Heap.
   Inicia nos nós internos (do índice `(n // 2) - 1` até 0) aplicando `heapify`.
2. Extração e Ordenação:
   - Troca o elemento da raiz (o maior) com o último elemento do heap.
   - Reduz o tamanho do heap considerado em 1.
   - Aplica `heapify` na nova raiz para restabelecer a propriedade de Max-Heap.
   - Repete o processo até que todos os elementos estejam ordenados.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n log n)
- Caso Médio:     O(n log n)
- Pior Caso:      O(n log n)  (garantia matemática consistente)
- Espaço Auxiliar: O(1)        (in-place: ordena dentro do próprio array)
- Estabilidade:   Não estável (as trocas na árvore alteram a ordem relativa)

Comparação com Quick Sort e Merge Sort:
- Mais rápido no pior caso que o Quick Sort (que pode degradar para O(n^2)).
- Usa menos memória auxiliar que o Merge Sort (O(1) vs O(n)).
- Na prática em média, Quick Sort costuma ser ligeiramente mais rápido devido
  ao cache de CPU e menor constante oculta.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Garante a propriedade de Max-Heap para a subárvore com raiz no índice `i`.
    `n` é o tamanho do heap considerado (elementos após `n` já estão na sua posição final).
    """
    maior = i          # Inicializa o maior como sendo a raiz atual
    esquerda = 2 * i + 1   # Filho esquerdo
    direita = 2 * i + 2    # Filho direito

    # Se o filho da esquerda existe e é maior que a raiz
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Se o filho da direita existe e é maior que o maior até agora
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Se o maior não for a raiz, troca e continua descendo no heap (recursão)
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heap_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista in-place utilizando Heap Sort.
    Retorna a mesma referência ordenada.
    """
    n = len(arr)

    # Fase 1: Constrói o Max-Heap (de baixo para cima)
    # Começa no último nó que possui filhos: (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Fase 2: Extrai elementos um a um do topo do heap
    for i in range(n - 1, 0, -1):
        # Move a raiz atual (maior elemento) para o final do array
        arr[0], arr[i] = arr[i], arr[0]

        # Restaura a propriedade de Max-Heap na raiz sobre o heap reduzido
        heapify(arr, i, 0)

    return arr


def heap_sort_didatico(arr: List[int]) -> List[int]:
    """
    Versão com explicações passo a passo da transformação em Max-Heap
    e das sucessivas extrações do elemento máximo.
    """
    arr_copia = arr.copy()
    n = len(arr_copia)
    
    print(f"Array original: {arr_copia}")

    # Fase 1: Construção
    print("\n--- Fase 1: Construção do Max-Heap ---")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copia, n, i)
        print(f"Heapify no índice {i} ({arr_copia[i]}): {arr_copia}")

    print(f"\nMax-Heap formado com sucesso! Maior elemento na raiz: {arr_copia[0]}")
    print(f"Estado do Max-Heap: {arr_copia}")

    # Fase 2: Extração
    print("\n--- Fase 2: Extração e Reconstrução ---")
    for i in range(n - 1, 0, -1):
        max_elemento = arr_copia[0]
        arr_copia[0], arr_copia[i] = arr_copia[i], arr_copia[0]
        print(f"Troca raiz ({max_elemento}) com posição {i} ({arr_copia[0]}) -> {arr_copia}")
        heapify(arr_copia, i, 0)
        print(f"  Após heapify(tamanho={i}): {arr_copia}")

    return arr_copia


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DIDÁTICA DO HEAP SORT")
    print("=" * 65)

    # Exemplo 1: Visualização do fluxo passo a passo
    amostra = [12, 11, 13, 5, 6, 7]
    resultado_passo_a_passo = heap_sort_didatico(amostra)
    print(f"\nResultado Final Ordenado: {resultado_passo_a_passo}")

    # Exemplo 2: Testes com diferentes tipos de listas
    cenarios = {
        "Vetor Desordenado": [4, 10, 3, 5, 1, 8, 2],
        "Vetor Já Ordenado": [1, 2, 3, 4, 5, 6, 7],
        "Vetor Invertido": [100, 80, 60, 40, 20, 0],
        "Elementos Iguais": [9, 3, 9, 1, 9, 5, 3],
        "Com Negativos": [-8, 22, 0, -15, 7, 3, -1],
    }

    print("\n" + "=" * 65)
    print("TESTE EM DIFERENTES CENÁRIOS:")
    print("=" * 65)
    for nome, dados in cenarios.items():
        copia = dados.copy()
        heap_sort(copia)
        print(f"[{nome}]")
        print(f"  Original: {dados}")
        print(f"  Ordenado: {copia}\n")

