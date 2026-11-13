"""
ALGORITMO DE BUSCA: BUSCA BINÁRIA (BINARY SEARCH)
- Requisito: A lista DEVE estar ordenada!
- Complexidade: O(log n)
"""

from typing import List


# -----------------------------------------------------------------------------
# 1. VERSÃO ITERATIVA (Usa laço while - gasta O(1) de memória)
# -----------------------------------------------------------------------------
def busca_binaria_iterativa(arr: List[int], alvo: int) -> int:
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # Encontrou o elemento
        if arr[meio] == alvo:
            return meio

        # Alvo é maior: descarta a metade esquerda
        elif arr[meio] < alvo:
            inicio = meio + 1

        # Alvo é menor: descarta a metade direita
        else:
            fim = meio - 1

    return -1  # Não encontrado


# -----------------------------------------------------------------------------
# 2. VERSÃO RECURSIVA (A função chama a si mesma - gasta O(log n) de memória)
# -----------------------------------------------------------------------------
def busca_binaria_recursiva(arr: List[int], alvo: int, inicio: int = 0, fim: int = None) -> int:
    if fim is None:
        fim = len(arr) - 1

    # Caso base: o espaço de busca acabou e não encontrou
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    # Encontrou o elemento
    if arr[meio] == alvo:
        return meio

    # Alvo é maior: busca na metade direita
    elif arr[meio] < alvo:
        return busca_binaria_recursiva(arr, alvo, meio + 1, fim)

    # Alvo é menor: busca na metade esquerda
    else:
        return busca_binaria_recursiva(arr, alvo, inicio, meio - 1)


# -----------------------------------------------------------------------------
# TESTE SIMPLES
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50, 60, 70, 80]
    print(f"Lista ordenada: {numeros}\n")

    alvo = 40
    print(f"Buscando {alvo}:")
    print(f"  Iterativa: encontrado no índice {busca_binaria_iterativa(numeros, alvo)}")
    print(f"  Recursiva: encontrado no índice {busca_binaria_recursiva(numeros, alvo)}")

    alvo_inexistente = 99
    print(f"\nBuscando {alvo_inexistente}:")
    print(f"  Iterativa: {busca_binaria_iterativa(numeros, alvo_inexistente)} (não encontrado)")
    print(f"  Recursiva: {busca_binaria_recursiva(numeros, alvo_inexistente)} (não encontrado)")
