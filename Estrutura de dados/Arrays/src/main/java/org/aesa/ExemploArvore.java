package org.aesa;

public class ExemploArvore {

    // Classe que representa cada elemento (Nó) da árvore
    static class No {
        int valor;
        No esquerda; // Ponteiro para o filho da esquerda (valores menores)
        No direita;  // Ponteiro para o filho da direita (valores maiores)

        public No(int valor) {
            this.valor = valor;
            this.esquerda = null;
            this.direita = null;
        }
    }

    // Raiz da árvore (ponto de partida hierárquico)
    private No raiz;

    // Método para inserir um novo valor na Árvore Binária de Busca (BST)
    public void inserir(int valor) {
        raiz = inserirRecursivo(raiz, valor);
    }

    private No inserirRecursivo(No atual, int valor) {
        // Se o local estiver vazio, cria o novo nó
        if (atual == null) {
            return new No(valor);
        }

        // Se o valor for menor, desce para o lado esquerdo
        if (valor < atual.valor) {
            atual.esquerda = inserirRecursivo(atual.esquerda, valor);
        }
        // Se o valor for maior, desce para o lado direito
        else if (valor > atual.valor) {
            atual.direita = inserirRecursivo(atual.direita, valor);
        }

        return atual;
    }

    // Percurso Em-Ordem (In-Order Traversal): visita Esquerda -> Raiz -> Direita (ordem crescente)
    public void percorrerEmOrdem(No atual) {
        if (atual != null) {
            percorrerEmOrdem(atual.esquerda);
            System.out.print(atual.valor + " ");
            percorrerEmOrdem(atual.direita);
        }
    }

    // Método para buscar um elemento na árvore
    public boolean buscar(No atual, int valor) {
        if (atual == null) {
            return false;
        }
        if (atual.valor == valor) {
            return true;
        }
        return valor < atual.valor
                ? buscar(atual.esquerda, valor)
                : buscar(atual.direita, valor);
    }

    public static void main(String[] args) {
        ExemploArvore arvore = new ExemploArvore();

        // 1. Inserindo elementos na árvore
        // Raiz: 50
        arvore.inserir(50);
        arvore.inserir(30);
        arvore.inserir(70);
        arvore.inserir(20);
        arvore.inserir(40);
        arvore.inserir(60);
        arvore.inserir(80);

        // 2. Percorrendo a árvore (os dados saem ordenados automaticamente)
        System.out.print("Elementos da Árvore (Em-Ordem): ");
        arvore.percorrerEmOrdem(arvore.raiz);
        System.out.println();
        // Saída esperada: 20 30 40 50 60 70 80

        // 3. Buscando elementos de forma rápida (dividindo o caminho a cada nó)
        int valorBusca = 40;
        System.out.println("O valor " + valorBusca + " está na árvore? " + arvore.buscar(arvore.raiz, valorBusca));

        valorBusca = 99;
        System.out.println("O valor " + valorBusca + " está na árvore? " + arvore.buscar(arvore.raiz, valorBusca));
    }
}
