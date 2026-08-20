package org.aesa;

import java.util.LinkedList;
import java.util.Stack;

public class ExemploLinkedList {
    static void main() {
        // Criando a lista encadeada
        LinkedList<String> playlist = new LinkedList<>();

        // Adicionando músicas normalmente (vão para o fim da fila)
        playlist.add("Música A");
        playlist.add("Música B");
        playlist.add("Música C");

        // O usuário furou a fila e quer ouvir essa música AGORA (no topo da lista)
        playlist.addFirst("Música Furafila (Toca primeiro)");

        // O usuário adicionou uma música para o final absoluto
        playlist.addLast("Música de Encerramento");

        // Verificando a próxima música a tocar sem removê-la
        System.out.println("Próxima a tocar: " + playlist.getFirst());

        System.out.println("--- Lista Completa ---");

        // Percorrendo a lista encadeada (a ordem é respeitada pelos ponteiros)
        for (String musica : playlist) {
            System.out.println("- " + musica);
        }

        // Removendo a música que acabou de tocar
        playlist.removeFirst();
    }
}
