"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: MERGE SORT (ORDENAÇÃO POR INTERCALAÇÃO)
=============================================================================

Conceito:
---------
O Merge Sort é um algoritmo baseado no paradigma de "Divisão e Conquista"
(Divide and Conquer), criado por John von Neumann em 1945.

Como funciona:
1. Divisão: Divide o array recursivamente em duas metades até obter
   sub-arrays unitários (tamanho 1 ou 0), que já são considerados ordenados pois não tem mais velores [0] ou [].
2. Conquista/Combinação: Intercala (merge) as duas metades ordenadas
   em um único array resultante, comparando os elementos um a um.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n log n)
- Caso Médio:     O(n log n)
- Pior Caso:      O(n log n)
- Espaço Auxiliar: O(n) (precisa de memória extra para a intercalação)
- Estabilidade:   Estável (preserva a ordem relativa de elementos com chaves iguais)

Vantagens:
- Desempenho garantido de O(n log n) mesmo no pior caso possível.
- É um algoritmo estável.
- Muito eficiente para listas ligadas (Linked Lists) e ordenação externa (arquivos grandes em disco).

Desvantagens:
- Requer memória adicional O(n), o que pode ser proibitivo para vetores gigantes em memória RAM limitada.
"""

from typing import List, Tuple


def merge_sort(arr: List[int]) -> List[int]:
    """
    Ordena uma lista usando o algoritmo Merge Sort.
    
    :param arr: Lista de inteiros desordenada
    :return: Nova lista ordenada
    """
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas [0] / [1]
    if len(arr) <= 1:
        return arr

    # 1. Divisão: encontra o ponto médio e divide
    # NOTA: O cálculo `len(arr) // 2` e os fatiamentos `[:meio]` funcionam apenas em
    # ARRAYS / LISTAS INDEXADAS (acesso direto O(1)).
    # Para LISTAS ENCADEADAS (Linked Lists), essa abordagem NÃO FUNCIONA, pois não há
    # índices diretos; nelas, encontra-se o meio usando a técnica de dois ponteiros
    # (Slow & Fast Pointers / Lebre e Tartaruga: slow anda 1 passo e fast anda 2).
    meio = len(arr) // 2
    left_half = merge_sort(arr[:meio]) # Aqui acontece uma recursão para ordenar a metade esquerda - ate sobrar um elemento ou nenhum
    right_half = merge_sort(arr[meio:]) # Aqui acontece uma recursão para ordenar a metade direita - ate sobrar um elemento ou nenhum

    # 2. Conquista: combina as metades ordenadas
    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Função auxiliar que intercala duas listas ordenadas em uma única lista ordenada.
    """
    merged = []
    i = 0  # Ponteiro para a lista da esquerda
    j = 0  # Ponteiro para a lista da direita

    # Compara elementos de ambos os lados e insere o menor
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # <= garante estabilidade, pois mantém a ordem relativa de elementos iguais
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
