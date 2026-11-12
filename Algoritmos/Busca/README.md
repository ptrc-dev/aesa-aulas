# Algoritmos de Busca

Este diretório contém implementações completas, modulares e didáticas dos principais **Algoritmos de Busca** estudados em Ciência da Computação e Estruturas de Dados.

---

## 📁 Estrutura dos Arquivos

| Arquivo | Algoritmo | Complexidade Média | Pré-requisito Principal |
| :--- | :--- | :---: | :--- |
| [`busca_linear.py`](./busca_linear.py) | **Busca Linear / Sequencial** | $O(n)$ | Nenhum (funciona com lista desordenada) |
| [`busca_binaria.py`](./busca_binaria.py) | **Busca Binária (Iterativa e Recursiva)** | $O(\log n)$ | **Lista previamente ordenada** e indexada |
| [`busca_hashing.py`](./busca_hashing.py) | **Busca por Hashing (Tabela Hash)** | $O(1)$ | Função de dispersão (hash) e memória auxiliar |
| [`comparativo_buscas.py`](./comparativo_buscas.py) | **Benchmark e Análise Comparativa** | - | Executa os 3 algoritmos medindo tempo real ($\mu s$) |

---

## 1. 🔍 Busca Linear (Sequencial)

- **Conceito:** Percorre o vetor elemento a elemento desde o índice `0` até o final, comparando cada valor com o elemento procurado.
- **Variações incluídas:**
  - Busca Linear Clássica (retorna o primeiro índice ou `-1`).
  - Busca de Todas as Ocorrências (retorna lista de índices com chaves repetidas).
  - **Busca Linear com Sentinela** (otimização que elimina a verificação `i < n` em cada passo).
  - Versão Didática com rastreamento visual das comparações.

---

## 2. ⚡ Busca Binária (Binary Search)

- **Conceito:** Utiliza o paradigma de **Divisão e Conquista**. A cada passo, calcula o elemento do meio (`(inicio + fim) // 2`):
  - Se for igual ao alvo: encerra.
  - Se o alvo for menor: descarta a metade direita (`fim = meio - 1`).
  - Se o alvo for maior: descarta a metade esquerda (`inicio = meio + 1`).
- **Poder do $O(\log n)$:**
  - Em $1.000.000$ de elementos, a busca linear pode levar até $1.000.000$ de passos, enquanto a binária resolve em no máximo **$20$ passos**.
- **Variações incluídas:**
  - Versão Iterativa (espaço auxiliar $O(1)$).
  - Versão Recursiva.
  - Versão Didática mostrando os ponteiros e os sub-vetores descartados.

---

## 3. 🎯 Busca por Hashing (Tabela Hash)

- **Conceito:** Em vez de realizar comparações sucessivas entre chaves, aplica uma **Função Hash** sobre a chave que calcula **diretamente o índice de memória** onde o dado deve estar gravado.
- **Colisões:** Quando chaves distintas geram o mesmo índice ($h(k_1) = h(k_2)$).
- **Implementações incluídas:**
  - **Encadeamento Separado (`TabelaHashEncadeada`):** cada índice do array é um balde (*bucket*) contendo uma lista encadeada.
  - **Endereçamento Aberto (`TabelaHashSondagemLinear`):** resolve colisões procurando o próximo slot vazio sequencialmente.

---

## 📊 Tabela Comparativa de Complexidade

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso | Espaço Auxiliar | Pré-requisito |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Busca Linear** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | Nenhum |
| **Busca Binária** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ iterativo / $O(\log n)$ recursivo | Vetor **Ordenado** e Acesso $O(1)$ |
| **Busca Hashing** | $O(1)$ | $O(1)$ | $O(n)$* | $O(m + n)$ | Função Hash adequada |

*\* O pior caso do Hashing ocorre apenas no caso patológico de todas as chaves colidirem no mesmo balde.*

---

## 🚀 Como Executar

No terminal, navegue até a pasta `Busca`:

```bash
cd Algoritmos/Busca

# 1. Executar a Busca Linear:
python3 busca_linear.py

# 2. Executar a Busca Binária:
python3 busca_binaria.py

# 3. Executar a Busca por Hashing:
python3 busca_hashing.py

# 4. Executar o Benchmark Comparativo:
python3 comparativo_buscas.py
```

