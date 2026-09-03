package org.aesa.atividades;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * DESAFIO 04 - PILHA (STACK / LIFO)
 * 
 * Objetivo: Praticar a estrutura de dados Pilha (Last In, First Out) utilizando Deque e ArrayDeque.
 * 
 * Cenário: Histórico de "Desfazer" (Control + Z) de um Editor de Texto.
 * 
 * Instruções:
 * 1. Crie uma pilha usando Deque<String> chamada historicoEditor = new ArrayDeque<>().
 * 2. Simule a execução de 4 ações do usuário empilhando-as (push()):
 *    - "Digitar título"
 *    - "Inserir imagem"
 *    - "Mudar fonte para Arial"
 *    - "Deletar parágrafo"
 * 3. Exiba qual foi a última ação realizada (topo da pilha usando peek()).
 * 4. Simule 2 cliques seguidos no botão "Desfazer" (Control + Z), desempilhando as ações (pop()) e exibindo a mensagem "Desfazendo ação: ...".
 * 5. Exiba qual ação agora está no topo do histórico.
 * 6. Verifique se a pilha está vazia com o método isEmpty().
 */
public class Desafio04_Pilha {

    public static void main(String[] args) {
        // TODO: Crie a pilha usando Deque<String> e ArrayDeque<>
        Deque<String> historicoEditor = new ArrayDeque<>();

        // TODO: Empilhe 4 ações com push()
        historicoEditor.push("Digitar título");
        historicoEditor.push("Inserir imagem");
        historicoEditor.push("Mudar fonte para Arial");
        historicoEditor.push("Deletar parágrafo");

        // TODO: Consulte a ação do topo sem remover usando peek()
        System.out.println("Última ação realizada (Topo): " + historicoEditor.peek());

        // TODO: Simule 2 operações de Desfazer usando pop()
        System.out.println("--- Pressionando Ctrl + Z 2 vezes ---");
        String desfeita1 = historicoEditor.pop();
        System.out.println("Desfazendo: " + desfeita1);

        String desfeita2 = historicoEditor.pop();
        System.out.println("Desfazendo: " + desfeita2);

        // TODO: Verifique a ação que está no topo agora
        System.out.println("Ação no topo agora: " + historicoEditor.peek());

        // TODO: Imprima se o histórico está vazio ou não
        System.out.println("O histórico está vazio? " + historicoEditor.isEmpty());
    }
}
