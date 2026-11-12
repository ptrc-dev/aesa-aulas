"""
=============================================================================
ALGORITMO DE BUSCA: BUSCA LINEAR (OU SEQUENCIAL)
=============================================================================

Conceito:
---------
A Busca Linear é o algoritmo de busca mais intuitivo, simples e universal.
Consiste em inspecionar sequencialmente cada elemento da coleção, do início
até o fim, comparando-o com o valor procurado (alvo) até que o elemento seja
encontrado ou a coleção seja totalmente percorrida.

Como funciona:
1. Inicia no primeiro elemento (índice 0).
2. Compara o elemento atual `arr[i]` com o `alvo`.
3. Se forem iguais, encerra imediatamente e retorna o índice `i`.
4. Se forem diferentes, avança para o próximo elemento (`i + 1`).
5. Se percorrer toda a lista sem encontrar, retorna `-1` (indicando ausência).

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(1)       (o elemento está na primeira posição: índice 0)
- Caso Médio:     O(n)       (em média, inspeciona n/2 elementos)
- Pior Caso:      O(n)       (o elemento está na última posição ou não existe)
- Espaço Auxiliar: O(1)       (opera in-place, usa apenas variáveis de iteração)

Pré-requisito:
--------------
NENHUM. Não exige que a lista esteja ordenada e nem que possua índices
especiais. Funciona em vetores, listas dinâmicas, listas encadeadas, etc.

Vantagens:
----------
- Extremamente simples de entender e implementar.
- Funciona em coleções desordenadas e dados que chegam em fluxo (streaming).
- Eficiente para coleções pequenas (baixo overhead de código/memória).

Desvantagens:
-------------
- Ineficiente para grandes volumes de dados: o tempo de busca cresce
  proporcionalmente ao tamanho da lista (O(n)).
"""

from typing import Any, List, Optional


def busca_linear(arr: List[Any], alvo: Any) -> int:
    """
    Realiza a busca linear clássica por um elemento em uma lista.

    :param arr: Lista com os elementos (ordenados ou desordenados).
    :param alvo: Elemento a ser procurado.
    :return: Índice da primeira ocorrência do elemento, ou -1 se não encontrado.
    """
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i  # Encontrado! Retorna o índice imediatamente
    return -1  # Não encontrado após percorrer toda a lista


def busca_linear_todas_ocorrencias(arr: List[Any], alvo: Any) -> List[int]:
    """
    Variação que busca TODAS as ocorrências de um elemento na lista,
    retornando todos os índices onde ele aparece.

    :param arr: Lista com os elementos.
    :param alvo: Elemento procurado.
    :return: Lista de índices onde o elemento foi encontrado.
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == alvo:
            indices.append(i)
    return indices


def busca_linear_com_sentinela(arr: List[Any], alvo: Any) -> int:
    """
    Otimização clássica conhecida como "Busca com Sentinela".

    Em um loop de busca tradicional, a cada iteração são feitas DUAS checagens:
    1. Se o índice ainda é válido (`i < n`).
    2. Se o elemento é o alvo (`arr[i] == alvo`).

    Com a Sentinela:
    Inserimos temporariamente o próprio 'alvo' no final do vetor como uma sentinela.
    Assim, temos CERTEZA de que o loop 'while' encontrará o alvo sem precisar
    testar os limites do vetor a cada passo (`i < n`), reduzindo o número de instruções.
    """
    n = len(arr)
    if n == 0:
        return -1

    # Guarda o último elemento e o substitui pela sentinela (alvo)
    ultimo_original = arr[-1]
    arr[-1] = alvo

    i = 0
    # Agora só precisamos comparar com o alvo (sem testar 'i < n' a cada iteração)
    while arr[i] != alvo:
        i += 1

    # Restaura o valor original do último elemento
    arr[-1] = ultimo_original

    # Se parou antes do último elemento, encontramos uma ocorrência real
    if i < n - 1:
        return i

    # Se parou no último, verifica se o último original era de fato o alvo
    if ultimo_original == alvo:
        return n - 1

    return -1


def busca_linear_didatica(arr: List[Any], alvo: Any) -> int:
    """
    Versão didática que imprime passo a passo cada comparação realizada,
    ilustrando exatamente o caminho percorrido pelo algoritmo.
    """
    print(f"\n--- Iniciando Busca Linear Didática ---")
    print(f"Lista : {arr}")
    print(f"Alvo  : {alvo}")
    print("-" * 45)

    for i in range(len(arr)):
        elemento = arr[i]
        print(f"Passo {i + 1:02d}: Verificando índice [{i}] -> valor '{elemento}'", end="")

        if elemento == alvo:
            print("  ==> [ENCONTRADO!]")
            print(f"-> Elemento '{alvo}' localizado no índice {i} após {i + 1} comparações.")
            return i
        else:
            print("  (Diferente, avançando...)")

    print(f"-> Fim da lista atingido. Elemento '{alvo}' NÃO está presente ({len(arr)} comparações feitas).")
    return -1


# =============================================================================
# DEMONSTRAÇÕES E CASOS DE TESTE
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DO ALGORITMO: BUSCA LINEAR")
    print("=" * 65)

    # 1. Demonstração Didática com Passo a Passo
    dados = [42, 17, 89, 5, 23, 76, 12]
    busca_linear_didatica(dados, alvo=5)    # Elemento presente
    busca_linear_didatica(dados, alvo=99)   # Elemento ausente

    # 2. Teste da Versão com Sentinela
    print("\n" + "=" * 65)
    print("TESTE DA BUSCA LINEAR COM SENTINELA:")
    print("=" * 65)
    amostra = [10, 20, 30, 40, 50]
    idx_sentinela = busca_linear_com_sentinela(amostra, alvo=40)
    print(f"Vetor: {amostra}")
    print(f"Buscando '40' com sentinela: Encontrado no índice {idx_sentinela}")

    # 3. Teste de Múltiplas Ocorrências
    print("\n" + "=" * 65)
    print("TESTE DE BUSCA COM CHAVES DUPLICADAS:")
    print("=" * 65)
    nomes = ["Ana", "Carlos", "Beatriz", "Carlos", "Daniel", "Carlos"]
    ocorrencias = busca_linear_todas_ocorrencias(nomes, "Carlos")
    print(f"Lista de Nomes : {nomes}")
    print(f"Ocorrências de 'Carlos': Índices {ocorrencias}")

    # 4. Melhores e Piores Casos
    print("\n" + "=" * 65)
    print("ANÁLISE DE COMPLEXIDADE NA PRÁTICA:")
    print("=" * 65)
    numeros = [10, 20, 30, 40, 50, 60, 70, 80]
    print(f"Lista: {numeros}")
    print(f"Melhor Caso (alvo no início: 10) -> Índice: {busca_linear(numeros, 10)} (1 comparação)")
    print(f"Pior Caso   (alvo no fim: 80)    -> Índice: {busca_linear(numeros, 80)} (8 comparações)")
    print(f"Pior Caso   (alvo inexistente: 99) -> Retorno: {busca_linear(numeros, 99)} (8 comparações)")

