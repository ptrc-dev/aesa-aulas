package org.aesa.atividades;

import java.util.LinkedList;
import java.util.Queue;

/**
 * DESAFIO 05 - FILA (QUEUE / FIFO)
 * 
 * Objetivo: Praticar a estrutura de dados Fila (First In, First Out) utilizando a interface Queue.
 * 
 * Cenário: Sistema de Pedidos em um Drive-Thru de Fast Food.
 * 
 * Instruções:
 * 1. Crie uma fila de pedidos usando Queue<String> chamada filaDriveThru = new LinkedList<>().
 * 2. Adicione 4 pedidos na fila usando o método offer():
 *    - "Pedido #101 - Hambúrguer e Refri"
 *    - "Pedido #102 - Batata Frita"
 *    - "Pedido #103 - Milkshake de Chocolate"
 *    - "Pedido #104 - Combo Família"
 * 3. Exiba quem é o próximo pedido a ser preparado/atendido usando o método peek().
 * 4. Simule o atendimento e entrega dos 2 primeiros pedidos usando o método poll(), imprimindo "Entregando: ...".
 * 5. Exiba qual é o próximo pedido que está aguardando no início da fila.
 * 6. Imprima todos os pedidos restantes aguardando na fila.
 */
public class Desafio05_Fila {

    public static void main(String[] args) {
        // TODO: Crie a fila usando Queue<String> e LinkedList<>
        Queue<String> filaDriveThru = new LinkedList<>();

        // TODO: Enfileire 4 pedidos usando offer()
        filaDriveThru.offer("Pedido #101 - Hambúrguer e Refri");
        filaDriveThru.offer("Pedido #102 - Batata Frita");
        filaDriveThru.offer("Pedido #103 - Milkshake de Chocolate");
        filaDriveThru.offer("Pedido #104 - Combo Família");

        // TODO: Verifique o próximo da fila sem remover (peek())
        System.out.println("Próximo pedido a ser atendido: " + filaDriveThru.peek());

        // TODO: Atenda os 2 primeiros pedidos com poll()
        System.out.println("--- Atendendo Pedidos ---");
        String entregue1 = filaDriveThru.poll();
        System.out.println("Entregando: " + entregue1);

        String entregue2 = filaDriveThru.poll();
        System.out.println("Entregando: " + entregue2);

        // TODO: Verifique quem ficou na frente da fila agora
        System.out.println("Próximo da fila agora: " + filaDriveThru.peek());

        // TODO: Imprima todos os pedidos que ainda faltam ser atendidos
        System.out.println("--- Pedidos Restantes na Fila ---");
        for (String pedido : filaDriveThru) {
            System.out.println("- " + pedido);
        }
    }
}
