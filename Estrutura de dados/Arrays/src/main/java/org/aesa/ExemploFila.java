package org.aesa;

import java.util.LinkedList;
import java.util.Queue;

public class ExemploFila {
    public static void main(String[] args) {
        // Criando a Fila usando a interface Queue
        Queue<String> filaDoBanco = new LinkedList<>();

        // Clientes chegando (vão para o final da fila)
        filaDoBanco.offer("Ana");
        filaDoBanco.offer("Carlos");
        filaDoBanco.offer("Beatriz");

        System.out.println("Quem é o próximo a ser atendido? " + filaDoBanco.peek());
        // Saída: Ana

        // Atendendo o cliente (remove do início da fila)
        String clienteAtendido = filaDoBanco.poll();
        System.out.println("Atendendo: " + clienteAtendido);

        // Verificando a fila agora
        System.out.println("Próximo da fila agora: " + filaDoBanco.peek());
        // Saída: Carlos
    }
}
