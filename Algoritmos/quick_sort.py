"""
=============================================================================
ALGORITMO DE ORDENAÇÃO: QUICK SORT (ORDENAÇÃO RÁPIDA)
=============================================================================

Conceito:
---------
Desenvolvido por Tony Hoare em 1959, o Quick Sort é um dos algoritmos de
ordenação mais populares e amplamente utilizados na prática.

Também adota o paradigma de "Divisão e Conquista", mas diferentemente do
Merge Sort (que divide sempre ao meio exato e faz o trabalho pesado na união),
o Quick Sort faz o trabalho pesado no "Particionamento":
1. Escolha de um elemento chamado PIVÔ.
2. Particionamento: Reorganiza o array de forma que todos os elementos
   menores que o pivô fiquem à sua esquerda, e todos os maiores à direita.
3. Recursão: Aplica o mesmo processo recursivamente nas partições à esquerda
   e à direita do pivô.

Complexidade Assintótica:
-------------------------
- Melhor Caso:    O(n log n)  (quando o pivô divide o vetor aproximadamente ao meio)
- Caso Médio:     O(n log n)  (na grande maioria das distribuições de dados)
- Pior Caso:      O(n^2)      (quando o pivô escolhido é repetidamente o menor ou maior elemento)
- Espaço:         O(log n)    (memória da pilha de chamadas na versão in-place)
- Estabilidade:   Não estável (pode alterar a ordem relativa de elementos iguais)

Como mitigar o Pior Caso:
- Escolher o pivô aleatoriamente (Randomized Quick Sort)
- Usar a "Mediana de Três" (primeiro, meio e último elemento)
"""

from typing import List


# -----------------------------------------------------------------------------
# 1. VERSÃO DIDÁTICA (PYTHONIC - LIST COMPREHENSION)
# Fácil de ler e entender conceitualmente o particionamento.
# Cria novas listas na memória (não é in-place).
# -----------------------------------------------------------------------------
def quick_sort_didatico(arr: List[int], nivel: int = 0) -> List[int]:
    """
    Implementação didática com rastreamento visual das chamadas.
    """
    indent = "  " * nivel
    if len(arr) <= 1:
        print(f"{indent}Base: {arr}")
        return arr

    # Escolha do pivô (aqui usamos o elemento central)
    pivo = arr[len(arr) // 2]
    
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]

    print(f"{indent}Pivô: {pivo} | Menores: {menores} | Iguais: {iguais} | Maiores: {maiores}")

    ordenados_esquerda = quick_sort_didatico(menores, nivel + 1)
    ordenados_direita = quick_sort_didatico(maiores, nivel + 1)

    resultado = ordenados_esquerda + iguais + ordenados_direita
    print(f"{indent}Junção: {resultado}")
    return resultado


# -----------------------------------------------------------------------------
# 2. VERSÃO CLÁSSICA IN-PLACE (PARTICIONAMENTO DE LOMUTO)
# Esta é a implementação de referência acadêmica e de alto desempenho:
# Não cria cópias de arrays, ordenando os elementos dentro do próprio vetor original.
# -----------------------------------------------------------------------------
def quick_sort_in_place(arr: List[int], inicio: int = 0, fim: int = None) -> List[int]:
    """
    Implementação clássica in-place do Quick Sort utilizando o esquema de Lomuto.
    """
    if fim is None:
        fim = len(arr) - 1

    if inicio < fim:
        # p_index é o índice definitivo onde o pivô foi alocado
        p_index = _particionar_lomuto(arr, inicio, fim)

        # Ordena recursivamente os elementos antes e depois do pivô
        quick_sort_in_place(arr, inicio, p_index - 1)
        quick_sort_in_place(arr, p_index + 1, fim)

    return arr


def _particionar_lomuto(arr: List[int], inicio: int, fim: int) -> int:
    """
    Particionamento de Lomuto:
    - O pivô é o elemento na última posição (arr[fim]).
    - 'i' rastreia a fronteira dos elementos que são menores que o pivô.
    """
    pivo = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        # Se o elemento atual for menor ou igual ao pivô, expande a região dos menores
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Posiciona o pivô no seu local ordenado final (i + 1)
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1


# =============================================================================
# DEMONSTRAÇÕES E EXEMPLOS PRÁTICOS
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO DIDÁTICA DO QUICK SORT")
    print("=" * 65)

    # Exemplo 1: Visualização do particionamento passo a passo
    amostra = [33, 10, 55, 71, 46, 18, 29]
    print(f"\nArray Inicial: {amostra}")
    print("\nExecução Passo a Passo (Rastreando Pivôs e Partições):")
    resultado = quick_sort_didatico(amostra)
    print(f"\nResultado Final: {resultado}")

    # Exemplo 2: Teste da versão in-place
    print("\n" + "=" * 65)
    print("TESTE DA VERSÃO CLÁSSICA IN-PLACE (PARTICIONAMENTO DE LOMUTO):")
    print("=" * 65)
    vetor_teste = [84, 23, 9, 41, 15, 63, 2, 70]
    print(f"Antes da ordenação : {vetor_teste}")
    quick_sort_in_place(vetor_teste)
    print(f"Após a ordenação   : {vetor_teste}")

    # Exemplo 3: Cenários diversos
    cenarios = {
        "Lista Já Ordenada": [10, 20, 30, 40, 50],
        "Lista Decrescente": [50, 40, 30, 20, 10],
        "Chaves Duplicadas": [7, 2, 7, 3, 2, 8, 7, 1],
        "Valores Negativos": [-10, 45, -2, 0, 18, -30],
    }

    print("\n" + "=" * 65)
    print("CENÁRIOS DE TESTE COM A VERSÃO IN-PLACE:")
    print("=" * 65)
    for nome, dados in cenarios.items():
        copia = dados.copy()
        quick_sort_in_place(copia)
        print(f"[{nome}]")
        print(f"  Entrada: {dados}")
        print(f"  Saída  : {copia}\n")

