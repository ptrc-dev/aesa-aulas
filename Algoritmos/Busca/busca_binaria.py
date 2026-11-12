"""
=============================================================================
ALGORITMO DE BUSCA: BUSCA BINÁRIA (BINARY SEARCH)
=============================================================================

Conceito:
---------
A Busca Binária é um algoritmo de busca extremamente eficiente baseado no
paradigma de "Divisão e Conquista" (Divide and Conquer).

A cada iteração, o algoritmo examina o elemento que está no MEIO do vetor:
- Se o elemento do meio for igual ao alvo, a busca termina com sucesso.
- Se o alvo for menor que o elemento do meio, descarta-se toda a metade direita.
- Se o alvo for maior que o elemento do meio, descarta-se toda a metade esquerda.

Dessa forma, o espaço de busca é reduzido PELA METADE a cada passo!

PRÉ-REQUISITO FUNDAMENTAL:
--------------------------
O vetor DEVE ESTAR PREVIAMENTE ORDENADO! Se a coleção estiver desordenada,
a premissa de descarte de metades falha e o algoritmo trará respostas incorretas.
Além disso, exige acesso direto por índice em O(1) (arrays/listas indexadas).

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(1)       (o elemento procurado está exatamente no meio na 1ª tentativa)
- Caso Médio:     O(log n)   (divide a lista pela metade sucessivamente)
- Pior Caso:      O(log n)   (o elemento está nas extremidades ou não existe)
- Espaço Auxiliar:
  * Versão Iterativa: O(1)   (utiliza apenas ponteiros de controle)
  * Versão Recursiva: O(log n) (memória da pilha de chamadas da recursão)

A Magia do O(log n):
--------------------
- Vetor de 1.000 elementos:       máximo de ~10 comparações (2^10 = 1024)
- Vetor de 1.000.000 elementos:   máximo de ~20 comparações (2^20 ≈ 1.048.576)
- Vetor de 1.000.000.000 elementos: máximo de ~30 comparações!

Vantagens:
----------
- Velocidade excepcional para coleções médias e grandes.
- Número de comparações muito pequeno comparado à busca linear.

Desvantagens:
-------------
- Exige que a coleção esteja estritamente ordenada.
- Ordenar uma lista custa O(n log n). Se você for fazer poucas buscas pontuais,
  pode ser mais rápido usar a busca linear do que ordenar primeiro.
- Não é eficiente em listas encadeadas (Linked Lists), pois acessar o elemento
  do meio em uma lista encadeada exige percorrer nó por nó em O(n).
"""

from typing import List, Optional


def busca_binaria_iterativa(arr: List[int], alvo: int) -> int:
    """
    Implementação iterativa clássica da Busca Binária (versão in-place com ponteiros).

    :param arr: Lista de inteiros PREVIAMENTE ORDENADA.
    :param alvo: Inteiro a ser localizado.
    :return: Índice do elemento encontrado, ou -1 se não estiver presente.
    """
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        # Ponto médio (evita overflow em linguagens como C/Java fazendo: inicio + (fim - inicio) // 2)
        meio = (inicio + fim) // 2

        if arr[meio] == alvo:
            return meio  # Encontrado!
        elif arr[meio] < alvo:
            inicio = meio + 1  # O alvo está na metade direita
        else:
            fim = meio - 1  # O alvo está na metade esquerda

    return -1  # Intervalo esgotado sem encontrar o alvo


def busca_binaria_recursiva(
    arr: List[int], alvo: int, inicio: int = 0, fim: Optional[int] = None
) -> int:
    """
    Implementação recursiva da Busca Binária.

    :param arr: Lista ordenada.
    :param alvo: Valor procurado.
    :param inicio: Limite inferior do intervalo de busca.
    :param fim: Limite superior do intervalo de busca.
    :return: Índice do elemento, ou -1 se não encontrado.
    """
    if fim is None:
        fim = len(arr) - 1

    # Caso base: intervalo de busca esgotado (alvo inexistente)
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if arr[meio] == alvo:
        return meio
    elif arr[meio] < alvo:
        # Chama recursivamente para a metade direita
        return busca_binaria_recursiva(arr, alvo, inicio=meio + 1, fim=fim)
    else:
        # Chama recursivamente para a metade esquerda
        return busca_binaria_recursiva(arr, alvo, inicio=inicio, fim=meio - 1)


def busca_binaria_didatica(arr: List[int], alvo: int) -> int:
    """
    Versão didática que ilustra o processo de divisão sucessiva da busca binária,
    mostrando os ponteiros de início, meio e fim e o sub-vetor atual a cada passo.
    """
    print(f"\n--- Iniciando Busca Binária Didática ---")
    print(f"Vetor Ordenado: {arr}")
    print(f"Alvo Procurado: {alvo}")
    print("-" * 65)

    inicio = 0
    fim = len(arr) - 1
    passo = 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        sub_vetor = arr[inicio : fim + 1]

        print(f"Passo {passo:02d}:")
        print(f"  Intervalo atual : índices [{inicio} .. {fim}] -> Sub-vetor: {sub_vetor}")
        print(f"  Ponteiro Meio   : índice [{meio}] -> valor = {arr[meio]}")

        if arr[meio] == alvo:
            print(f"  ==> SUCESSO! {arr[meio]} == {alvo}. Encontrado no índice [{meio}] em {passo} passos.")
            return meio
        elif arr[meio] < alvo:
            print(f"  Compara: {arr[meio]} < {alvo} -> O alvo é MAIOR. Descartando metade esquerda.")
            inicio = meio + 1
        else:
            print(f"  Compara: {arr[meio]} > {alvo} -> O alvo é MENOR. Descartando metade direita.")
            fim = meio - 1

        passo += 1
        print("-" * 65)

    print(f"-> Intervalo esgotado (inicio > fim). O alvo {alvo} NÃO está no vetor.")
    return -1


# =============================================================================
# DEMONSTRAÇÕES E CASOS DE TESTE
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DO ALGORITMO: BUSCA BINÁRIA")
    print("=" * 65)

    # Vetor precisa obrigatoriamente estar ORDENADO
    vetor_ordenado = [3, 9, 14, 19, 25, 31, 42, 57, 68, 73, 85, 91, 99]

    # 1. Demonstração Didática com Passo a Passo
    busca_binaria_didatica(vetor_ordenado, alvo=42)  # Elemento central
    busca_binaria_didatica(vetor_ordenado, alvo=99)  # Elemento na extremidade
    busca_binaria_didatica(vetor_ordenado, alvo=50)  # Elemento inexistente

    # 2. Teste Comparativo de Implementações: Iterativa vs Recursiva
    print("\n" + "=" * 65)
    print("TESTE DE EQUIVALÊNCIA (ITERATIVA vs RECURSIVA):")
    print("=" * 65)
    alvos_teste = [3, 31, 85, 100]

    for alvo in alvos_teste:
        idx_it = busca_binaria_iterativa(vetor_ordenado, alvo)
        idx_rec = busca_binaria_recursiva(vetor_ordenado, alvo)
        status = f"Índice: {idx_it}" if idx_it != -1 else "Não encontrado (-1)"
        print(f"Alvo {alvo:3d} -> Iterativa: {idx_it:2d} | Recursiva: {idx_rec:2d} -> [{status}]")

    # 3. Eficiência em Grande Escala (Comparação Teórica de Passos)
    print("\n" + "=" * 65)
    print("PODER DA BUSCA BINÁRIA EM GRANDES MASSAS DE DADOS:")
    print("=" * 65)
    tamanhos = [100, 1_000, 100_000, 1_000_000, 1_000_000_000]
    import math

    print(f"{'Tamanho da Lista (N)':<25} | {'Max Comparações (Linear)':<25} | {'Max Comparações (Binária)'}")
    print("-" * 78)
    for n in tamanhos:
        max_binaria = math.ceil(math.log2(n + 1))
        print(f"{n:<25,d} | {n:<25,d} | {max_binaria} passos")

