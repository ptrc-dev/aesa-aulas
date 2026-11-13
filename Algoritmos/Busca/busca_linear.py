"""
ALGORITMO DE BUSCA: BUSCA LINEAR (SEQUENCIAL)
- Requisito: Nenhum (funciona com listas desordenadas)
- Complexidade: O(n)
"""

from typing import Any, List


def busca_linear(arr: List[Any], alvo: Any) -> int:
    """
    Percorre a lista do início ao fim comparando elemento por elemento.
    Retorna o índice onde encontrou o alvo, ou -1 se não existir.
    """
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i  # Encontrou! Retorna o índice imediatamente

    return -1  # Percorreu tudo e não encontrou


# -----------------------------------------------------------------------------
# TESTE SIMPLES
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    lista = [42, 17, 89, 5, 23, 76]
    print(f"Lista: {lista}\n")

    # Busca com sucesso
    alvo = 5
    resultado = busca_linear(lista, alvo)
    print(f"Buscando {alvo}: índice {resultado}")

    # Busca sem sucesso
    alvo_inexistente = 99
    resultado = busca_linear(lista, alvo_inexistente)
    print(f"Buscando {alvo_inexistente}: índice {resultado} (não encontrado)")
