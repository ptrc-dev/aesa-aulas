package org.aesa;

import java.util.ArrayDeque;
import java.util.Deque;

public class ExemploPilha {
    public static void main(String[] args) {
        // Criando a Pilha moderna usando Deque e ArrayDeque
        Deque<String> historicoNavegador = new ArrayDeque<>();

        // Usuário navegando (cada nova página vai para o topo)
        historicoNavegador.push("Página Inicial");
        historicoNavegador.push("Página de Produtos");
        historicoNavegador.push("Carrinho de Compras");

        System.out.println("Página atual (topo): " + historicoNavegador.peek());
        // Saída: Carrinho de Compras

        // Usuário clicou no botão "Voltar" (remove do topo)
        String paginaFechada = historicoNavegador.pop();
        System.out.println("Fechando a página: " + paginaFechada);

        // Verificando para onde o usuário voltou
        System.out.println("Página atual agora: " + historicoNavegador.peek());
        // Saída: Página de Produtos
    }
}
