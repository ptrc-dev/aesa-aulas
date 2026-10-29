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
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort_didatico(arr: List[int], nivel: int = 0) -> List[int]:
    """
    Versão didática do Merge Sort que imprime na tela as divisões
    e intercalações com indentação visual para fins pedagógicos.
    """
    indent = "  " * nivel
    print(f"{indent}--> Dividindo: {arr}")

    if len(arr) <= 1:
        print(f"{indent}<-- Base atingida: {arr}")
        return arr

    mid = len(arr) // 2
    left = merge_sort_didatico(arr[:mid], nivel + 1)
    right = merge_sort_didatico(arr[mid:], nivel + 1)

    resultado = _merge(left, right)
    print(f"{indent}==> Intercalou {left} e {right} => {resultado}")
    return resultado


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DIDÁTICA DO MERGE SORT")
    print("=" * 60)

    # Exemplo 1: Visualização passo a passo da árvore de divisão e conquista
    exemplo_didatico = [38, 27, 43, 3, 9, 82, 10]
    print(f"\nArray Inicial: {exemplo_didatico}")
    print("\nExecução Passo a Passo (Árvore de Execução):")
    resultado_didatico = merge_sort_didatico(exemplo_didatico)
    print(f"\nResultado Final Ordenado: {resultado_didatico}")

    # Exemplo 2: Testes com diferentes cenários
    cenarios = {
        "Lista Aleatória": [64, 34, 25, 12, 22, 11, 90],
        "Lista Já Ordenada": [1, 2, 3, 4, 5, 6, 7],
        "Lista Invertida": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "Elementos Duplicados": [5, 1, 3, 5, 2, 1, 5, 3],
        "Lista com Negativos": [-5, 12, -30, 0, 8, -2, 15],
    }

    print("\n" + "=" * 60)
    print("TESTES EM DIFERENTES CENÁRIOS:")
    print("=" * 60)
    for nome, dados in cenarios.items():
        ordenado = merge_sort(dados)
        print(f"[{nome}]")
        print(f"  Entrada : {dados}")
        print(f"  Saída   : {ordenado}\n")

