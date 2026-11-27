"""
BUSCA LINEAR (SEQUENCIAL)
Exemplo simples para os valores: 3, 1, 9, 7
"""


def busca_linear(lista, alvo):
    """Percorre elemento por elemento até encontrar o alvo."""
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  # Encontrou: retorna o índice

    return -1  # Não encontrou


# -----------------------------------------------------------------------------
# TESTE COM: 3, 1, 9, 7
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    numeros = [3, 1, 9, 7]
    print(f"Lista: {numeros}\n")

    print(f"Buscando 9  -> índice: {busca_linear(numeros, 9)}")
    print(f"Buscando 5  -> índice: {busca_linear(numeros, 5)} (não encontrado)")


# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

if __name__ == "__main__":
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Lista: {numeros}\n")

    print(f"Buscando 9  -> índice: {busca_linear(numeros, 9)}")
    print(f"Buscando 5  -> índice: {busca_linear(numeros, 5)} (não encontrado)")