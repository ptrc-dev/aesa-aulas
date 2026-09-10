## Estrutura de Dados - Lineares

[HackerRank](https://www.hackerrank.com/domains/java)
[OnlineGdb](https://www.onlinegdb.com/online_java_compiler)
[Programiz](https://www.programiz.com/java-programming/online-compiler/)\

Estruturas Lineares são estruturas de armazenamento sequencial

A propriedade fundamental dessa estrutura é a relação entre posições relativas dos elementos em uma linha.

Arrays (Vetores) [Wiki Arrays](https://www.w3schools.com/java/java_arrays.asp)

- Os arrays (vetores) em Java são estruturas de dados que armazenam uma coleção de elementos do mesmo tipo
- O detalhe mais importante sobre eles é que **seu tamanho é fixo** — uma vez criados, não podem crescer ou diminuir.

Listas Encadeadas [Wiki LinkedList](https://www.w3schools.com/java/java_linkedlist.asp)

- Enquanto o Array e o ArrayList guardam os elementos "lado a lado" na memória, a **LinkedList espalha os elementos e os conecta por referências**.
- Imagine uma brincadeira de caça ao tesouro: você encontra a primeira pista (o dado), e junto com ela há um bilhete dizendo onde está a próxima pista. Cada elemento (chamado de "nó") guarda o seu valor e um "ponteiro" que indica quem é o próximo da fila.

Pilhas (Stacks) [Wiki Stack](https://www.geeksforgeeks.org/java/arraydeque-in-java/)

- As pilhas funcionam sob o princípio **LIFO (Last In, First Out)** — o último elemento a entrar é o primeiro a sair.
- Imagine uma pilha de pratos: você sempre adiciona um novo prato no topo (`push`) e, quando precisa retirar um, pega o que está no topo (`pop`).

Filas (Queues) [Wiki Queue](https://www.geeksforgeeks.org/java/queue-interface-java/)

- As filas funcionam sob o princípio **FIFO (First In, First Out)** — o primeiro elemento a entrar é o primeiro a sair.
- Imagine uma fila de caixa de supermercado: a primeira pessoa que chega é a primeira a ser atendida e sair (`poll`/`remove`), enquanto novas pessoas sempre entram no final da fila (`offer`/`add`).

## Estrutura de Dados - Não Lineares

Estruturas Não Lineares são estruturas de armazenamento não sequencial, onde os elementos se organizam de forma hierárquica ou em rede com múltiplos caminhos.

Tabelas Hash (Hash Tables / HashMap) [Wiki HashMap](https://www.w3schools.com/java/java_hashmap.asp)

- As Tabelas Hash armazenam dados no formato **chave-valor (Key-Value)** e utilizam uma função hash para calcular a posição na memória, oferecendo **busca, inserção e remoção extremamente rápidas (tempo médio O(1))**.
- Imagine um guarda-volumes de um clube: em vez de procurar sua mochila abrindo armário por armário, você tem um número/código único (chave) que leva você diretamente ao armário certo (valor).

Árvores (Trees) [Wiki Tree](https://www.geeksforgeeks.org/tree-data-structure/)

- As Árvores organizam os dados de forma **hierárquica e ramificada**, iniciando em um elemento principal chamado **raiz (root)**, que se conecta a nós filhos (*children*), formando folhas (*leaves*), sem a presença de ciclos.
- Imagine o sistema de pastas e arquivos do computador ou uma árvore genealógica: existe uma pasta raiz principal (ex: `C:` ou `/`) que contém pastas e subpastas filhas, onde cada uma pode ter múltiplos arquivos e pastas dentro de si.

Grafos (Graphs) [Wiki Graph](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)

- Os Grafos são estruturas em formato de **rede formadas por vértices (nós) e arestas (conexões)**, permitindo representar relações complexas de "muitos para muitos" (N para N), caminhos alternativos e ciclos.
- Imagine uma rede de linhas de metrô ou uma rede social: cada estação ou usuário é um vértice (nó), e as conexões de trilhos ou amizades/seguidores são as arestas que conectam os diferentes pontos da rede.

---

### Atividades Práticas (Desafios)

#### Estruturas Lineares:
- [Desafio 01 - Arrays (Vetores)](Arrays/src/main/java/org/aesa/atividades/Desafio01_Arrays.java)
- [Desafio 02 - ArrayList (Estrutura Dinâmica)](Arrays/src/main/java/org/aesa/atividades/Desafio02_ArrayList.java)
- [Desafio 03 - LinkedList (Lista Encadeada)](Arrays/src/main/java/org/aesa/atividades/Desafio03_LinkedList.java)
- [Desafio 04 - Pilha (Stack / LIFO)](Arrays/src/main/java/org/aesa/atividades/Desafio04_Pilha.java)
- [Desafio 05 - Fila (Queue / FIFO)](Arrays/src/main/java/org/aesa/atividades/Desafio05_Fila.java)

#### Estruturas Não Lineares:
- [Desafio 06 - Tabela Hash (HashMap)](Arrays/src/main/java/org/aesa/atividades/Desafio06_HashTable.java)
- [Desafio 07 - Árvore Binária de Busca (BST)](Arrays/src/main/java/org/aesa/atividades/Desafio07_Arvore.java)
- [Desafio 08 - Grafo (Lista de Adjacência)](Arrays/src/main/java/org/aesa/atividades/Desafio08_Grafo.java)
