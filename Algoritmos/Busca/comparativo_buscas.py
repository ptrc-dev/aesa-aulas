"""
=============================================================================
BENCHMARK COMPARATIVO: BUSCA LINEAR vs BUSCA BINÁRIA vs HASHING
=============================================================================

Este script coloca os três algoritmos de busca frente a frente:
1. Busca Linear:   O(n)
2. Busca Binária:  O(log n)
3. Busca Hashing:  O(1)

Mede o tempo real de execução e conta as comparações necessárias para encontrar
elementos em diferentes posições (início, meio, fim e elemento inexistente).
"""

import time
import random
from typing import List, Tuple
from busca_linear import busca_linear
from busca_binaria import busca_binaria_iterativa
from busca_hashing import TabelaHashEncadeada


def testar_desempenho(tamanho: int) -> None:
    print(f"\n{'='*75}")
    print(f"CENÁRIO DE TESTE: {tamanho:,} ELEMENTOS")
    print(f"{'='*75}")

    # 1. Preparação dos Dados
    # Geramos uma sequência ordenada de inteiros pares: [0, 2, 4, 6, ..., 2*(tamanho-1)]
    dados = list(range(0, tamanho * 2, 2))

    # Monta a Tabela Hash
    t0_hash = time.perf_counter()
    tabela_hash = TabelaHashEncadeada(capacidade=tamanho * 2)
    for num in dados:
        tabela_hash.inserir(num, f"Valor_{num}")
    tempo_carga_hash = (time.perf_counter() - t0_hash) * 1000

    # Chaves para teste:
    # - Início: dados[0]
    # - Meio: dados[tamanho // 2]
    # - Fim: dados[-1]
    # - Inexistente (ímpar): dados[-1] + 1
    casos = [
        ("Primeiro Elemento (Melhor Linear)", dados[0]),
        ("Elemento Central (Médio)", dados[tamanho // 2]),
        ("Último Elemento (Pior Linear)", dados[-1]),
        ("Elemento Ausente (Pior Caso Geral)", dados[-1] + 1),
    ]

    cabecalho = f"{'Cenário':<35} | {'Linear (µs)':<12} | {'Binária (µs)':<12} | {'Hashing (µs)':<12}"
    print(cabecalho)
    print("-" * 75)

    for descricao, alvo in casos:
        # Busca Linear
        t0 = time.perf_counter()
        busca_linear(dados, alvo)
        tempo_linear_us = (time.perf_counter() - t0) * 1_000_000

        # Busca Binária
        t0 = time.perf_counter()
        busca_binaria_iterativa(dados, alvo)
        tempo_binaria_us = (time.perf_counter() - t0) * 1_000_000

        # Busca Hashing
        t0 = time.perf_counter()
        tabela_hash.buscar(alvo)
        tempo_hash_us = (time.perf_counter() - t0) * 1_000_000

        print(
            f"{descricao:<35} | {tempo_linear_us:>10.2f} µs | {tempo_binaria_us:>10.2f} µs | {tempo_hash_us:>10.2f} µs"
        )


def imprimir_tabela_resumo() -> None:
    print("\n" + "=" * 80)
    print("QUADRO RESUMO COMPARATIVO DOS ALGORITMOS DE BUSCA")
    print("=" * 80)

    tabela = """
+---------------+----------------+----------------+----------------+-----------------+-----------------------+
| Algoritmo     | Melhor Caso    | Caso Médio     | Pior Caso      | Espaço Auxiliar | Pré-requisito         |
+---------------+----------------+----------------+----------------+-----------------+-----------------------+
| Busca Linear  | O(1)           | O(n)           | O(n)           | O(1)            | Nenhum (qualquer dado)|
| Busca Binária | O(1)           | O(log n)       | O(log n)       | O(1) (iterativo)| Vetor ORDENADO + O(1) |
| Busca Hashing | O(1)           | O(1)           | O(n)*          | O(m + n)        | Função Hash / Memória |
+---------------+----------------+----------------+----------------+-----------------+-----------------------+
* O pior caso do Hashing ocorre apenas em caso patológico onde todas as chaves colidem no mesmo bucket.
"""
    print(tabela)

    guia_decisao = """
GUIA DE DECISÃO RÁPIDA: QUANDO USAR CADA UM?
---------------------------------------------
1. Use BUSCA LINEAR quando:
   - A lista for pequena (ex: menos de 50 a 100 itens).
   - A lista estiver desordenada e você só precisa fazer UMA ou poucas buscas
     (ordenar custaria O(n log n), mais caro do que uma busca linear direta de O(n)).
   - A estrutura for uma lista simplesmente encadeada sem índices diretos.

2. Use BUSCA BINÁRIA quando:
   - Os dados já estiverem previamente ordenados (ou forem ordenados apenas uma vez
     e consultados centenas/milhares de vezes).
   - Você precisa economizar memória (não quer o overhead de uma tabela hash).
   - A estrutura permitir acesso aleatório O(1) por índice (vetores/arrays).

3. Use BUSCA HASHING quando:
   - Você precisa da MÁXIMA VELOCIDADE possível para consultas frequentes (tempo O(1)).
   - O volume de buscas e inserções for contínuo (ex: caches, banco de sessões, cadastros).
   - Você dispõe de memória RAM suficiente para armazenar a tabela com fator de carga seguro.
"""
    print(guia_decisao)


if __name__ == "__main__":
    imprimir_tabela_resumo()

    # Executa benchmarks para diferentes tamanhos
    testar_desempenho(1_000)
    testar_desempenho(50_000)

