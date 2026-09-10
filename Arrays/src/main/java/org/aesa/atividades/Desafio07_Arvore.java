package org.aesa.atividades;

/**
 * DESAFIO 07 - ÁRVORE (BINARY SEARCH TREE / HIERARQUIA)
 * 
 * Objetivo: Praticar a estrutura de dados Árvore Binária de Busca (BST),
 * compreendendo nós, referências recursivas, inserção ordenada, busca eficiente e percursos.
 * 
 * Cenário: Sistema de Classificação de Pontuações de um Jogo (High Scores).
 * 
 * Instruções:
 * 1. Defina a classe No contendo o valor (int pontuacao) e referências para No esquerda e No direita.
 * 2. Implemente o método de inserção recursiva mantendo a regra da BST:
 *    valores menores à esquerda e valores maiores à direita da raiz atual.
 * 3. Insira as seguintes pontuações de partidas: 50, 25, 75, 15, 35, 60, 90.
 * 4. Implemente o método percorrerEmOrdem() (In-Order) para listar as pontuações em ordem crescente.
 * 5. Implemente o método buscar() para verificar se certas pontuações (ex: 35 e 100) existem na árvore.
 * 6. Implemente métodos para encontrar a menor pontuação (navegando até a extrema esquerda)
 *    e a maior pontuação (navegando até a extrema direita).
 */
public class Desafio07_Arvore {

    // TODO: Defina a classe estática No
    static class No {
        int pontuacao;
        No esquerda;
        No direita;

        public No(int pontuacao) {
            this.pontuacao = pontuacao;
            this.esquerda = null;
            this.direita = null;
        }
    }

    private No raiz;

    // TODO: Implemente a inserção recursiva na BST
    public void inserir(int pontuacao) {
        raiz = inserirRecursivo(raiz, pontuacao);
    }

    private No inserirRecursivo(No atual, int pontuacao) {
        if (atual == null) {
            return new No(pontuacao);
        }

        if (pontuacao < atual.pontuacao) {
            atual.esquerda = inserirRecursivo(atual.esquerda, pontuacao);
        } else if (pontuacao > atual.pontuacao) {
            atual.direita = inserirRecursivo(atual.direita, pontuacao);
        }

        return atual;
    }

    // TODO: Implemente o percurso Em-Ordem (crescente: Esquerda -> Raiz -> Direita)
    public void percorrerEmOrdem(No atual) {
        if (atual != null) {
            percorrerEmOrdem(atual.esquerda);
            System.out.print(atual.pontuacao + " ");
            percorrerEmOrdem(atual.direita);
        }
    }

    // TODO: Implemente a busca eficiente de uma pontuação na BST
    public boolean buscar(No atual, int pontuacao) {
        if (atual == null) {
            return false;
        }
        if (atual.pontuacao == pontuacao) {
            return true;
        }
        return pontuacao < atual.pontuacao
                ? buscar(atual.esquerda, pontuacao)
                : buscar(atual.direita, pontuacao);
    }

    // TODO: Encontre a menor pontuação (nó mais à esquerda da árvore)
    public int encontrarMenor(No atual) {
        if (atual == null) {
            throw new IllegalStateException("A árvore está vazia!");
        }
        No temp = atual;
        while (temp.esquerda != null) {
            temp = temp.esquerda;
        }
        return temp.pontuacao;
    }

    // TODO: Encontre a maior pontuação (nó mais à direita da árvore)
    public int encontrarMaior(No atual) {
        if (atual == null) {
            throw new IllegalStateException("A árvore está vazia!");
        }
        No temp = atual;
        while (temp.direita != null) {
            temp = temp.direita;
        }
        return temp.pontuacao;
    }

    public static void main(String[] args) {
        Desafio07_Arvore leaderboard = new Desafio07_Arvore();

        // TODO: Insira 7 pontuações na árvore
        leaderboard.inserir(50);
        leaderboard.inserir(25);
        leaderboard.inserir(75);
        leaderboard.inserir(15);
        leaderboard.inserir(35);
        leaderboard.inserir(60);
        leaderboard.inserir(90);

        // TODO: Exiba as pontuações em ordem crescente (Em-Ordem)
        System.out.print("Pontuações registradas (ordem crescente): ");
        leaderboard.percorrerEmOrdem(leaderboard.raiz);
        System.out.println();

        // TODO: Realize buscas de pontuações
        System.out.println("\nA pontuação 35 foi alcançada? " + leaderboard.buscar(leaderboard.raiz, 35));
        System.out.println("A pontuação 100 foi alcançada? " + leaderboard.buscar(leaderboard.raiz, 100));

        // TODO: Encontre e exiba a menor e a maior pontuação registrada
        System.out.println("\nMenor pontuação (piso): " + leaderboard.encontrarMenor(leaderboard.raiz));
        System.out.println("Maior pontuação (recorde): " + leaderboard.encontrarMaior(leaderboard.raiz));
    }
}
