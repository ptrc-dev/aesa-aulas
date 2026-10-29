package org.aesa.atividades;

import java.util.ArrayList;

/**
 * DESAFIO 02 - ARRAYLIST (ESTRUTURA DINÂMICA)
 * 
 * Objetivo: Praticar a manipulação de listas dinâmicas, inserção, busca, remoção e travessia.
 * 
 * Instruções:
 * 1. Crie um ArrayList de String para representar uma Lista de Compras de Supermercado.
 * 2. Adicione 5 itens de sua escolha (ex: "Arroz", "Feijão", "Leite", "Café", "Açúcar").
 * 3. Verifique se o item "Leite" está presente na lista. Se estiver, remova-o.
 * 4. Adicione um novo item no final da lista.
 * 5. Exiba a quantidade atual de itens na lista (size()).
 * 6. Imprima cada item restante utilizando um loop for-each.
 */
public class Desafio02_ArrayList {

    public static void main(String[] args) {
        // TODO: Crie um ArrayList<String> chamado listaDeCompras
        ArrayList<String> listaDeCompras = new ArrayList<>();

        // TODO: Adicione 5 itens na lista
        listaDeCompras.add("Arroz");
        listaDeCompras.add("Feijão");
        listaDeCompras.add("Leite");
        listaDeCompras.add("Café");
        listaDeCompras.add("Açúcar");

        System.out.println("Lista inicial: " + listaDeCompras);

        // TODO: Verifique se a lista contém "Leite" (dica: use listaDeCompras.contains("Leite"))
        if (listaDeCompras.contains("Leite")) {
            // TODO: Remova o item "Leite" da lista
            listaDeCompras.remove("Leite");
            System.out.println("'Leite' foi removido da lista.");
        }

        // TODO: Adicione um novo item (ex: "Biscoito")
        listaDeCompras.add("Biscoito");

        // TODO: Exiba o número total de itens na lista (use .size())
        System.out.println("Total de itens na lista: " + listaDeCompras.size());

        // TODO: Percorra a lista com um loop for-each e imprima cada item formatado
        System.out.println("--- Itens da Lista de Compras ---");
        for (String item : listaDeCompras) {
            System.out.println("- " + item);
        }
    }
}
