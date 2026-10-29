package org.aesa;

import java.util.ArrayList;

public class ExemploArrayList {
    static void main() {
        // ArrayList é uma estrutura dinâmica: ele cresce automaticamente conforme
        // você adiciona novos itens e se ajusta quando você os remove.
        // Não aceita tipos primitivos diretamente (como int, double).
        // mas você pode usar suas classes wrapper (Integer, Double, etc.).

        // Criando uma lista vazia e dinâmica
        ArrayList<String> tarefas = new ArrayList<>();

        // Adicionando elementos
        tarefas.add("Estudar Java");
        tarefas.add("Resolver exercícios");
        tarefas.add("Tomar café");

        // Acessando um elemento específico
        System.out.println("Primeira tarefa: " + tarefas.get(0));

        // Removendo um elemento
        tarefas.remove("Tomar café");
        System.out.println("Total de tarefas agora: " + tarefas.size());

        // Percorrendo a lista com for-each
        for (String tarefa : tarefas) {
            System.out.println("- " + tarefa);
        }
    }
}
