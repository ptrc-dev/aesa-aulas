package org.aesa.atividades;

import java.util.LinkedList;

/**
 * DESAFIO 03 - LINKEDLIST (LISTA ENCADEADA)
 * 
 * Objetivo: Explorar as operações específicas de inserção e remoção no início e no fim da lista encadeada.
 * 
 * Cenário: Gerenciador de Playlist de Músicas com prioridade VIP.
 * 
 * Instruções:
 * 1. Crie uma LinkedList<String> chamada playlist.
 * 2. Adicione 3 músicas normais (ex: "Música 1", "Música 2", "Música 3").
 * 3. O usuário ativou a opção "Tocar Agora" para a música "Hit do Verão". Adicione-a no INÍCIO da playlist (addFirst).
 * 4. O usuário colocou a música "Encerramento" no FINAL absoluto da playlist (addLast).
 * 5. Consulte e exiba a PRIMEIRA música da playlist (getFirst()) e a ÚLTIMA música (getLast()) sem removê-las.
 * 6. Simule a execução da primeira música removendo-a do início (removeFirst()).
 * 7. Imprima a playlist completa atualizada com um loop for-each.
 */
public class Desafio03_LinkedList {

    public static void main(String[] args) {
        // TODO: Crie uma LinkedList de String chamada playlist
        LinkedList<String> playlist = new LinkedList<>();

        // TODO: Adicione 3 músicas normais com .add()
        playlist.add("Música 1");
        playlist.add("Música 2");
        playlist.add("Música 3");

        // TODO: Adicione a música "Hit do Verão" no INÍCIO usando addFirst()
        playlist.addFirst("Hit do Verão");

        // TODO: Adicione a música "Encerramento" no FINAL usando addLast()
        playlist.addLast("Encerramento");

        // TODO: Exiba a primeira e a última música sem remover (getFirst() e getLast())
        System.out.println("Próxima a tocar (Primeira): " + playlist.getFirst());
        System.out.println("Última da lista: " + playlist.getLast());

        // TODO: Simule que a primeira música tocou e remova-a com removeFirst()
        String tocada = playlist.removeFirst();
        System.out.println("Tocou agora: " + tocada);

        // TODO: Exiba toda a playlist restante
        System.out.println("--- Playlist Restante ---");
        for (String musica : playlist) {
            System.out.println("- " + musica);
        }
    }
}
