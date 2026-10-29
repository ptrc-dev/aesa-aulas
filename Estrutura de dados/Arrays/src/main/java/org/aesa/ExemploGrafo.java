package org.aesa;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ExemploGrafo {

    // Representação do Grafo usando Lista de Adjacência (Map onde cada vértice tem sua lista de conexões)
    private Map<String, List<String>> grafo = new HashMap<>();

    // Adiciona um novo vértice (nó/pessoa) à rede
    public void adicionarVertice(String vertice) {
        grafo.putIfAbsent(vertice, new ArrayList<>());
    }

    // Adiciona uma aresta (ligação de amizade bidirecional entre dois vértices)
    public void adicionarAresta(String origem, String destino) {
        adicionarVertice(origem);
        adicionarVertice(destino);

        grafo.get(origem).add(destino);
        grafo.get(destino).add(origem); // Grafo não-direcionado (conexão mútua)
    }

    // Exibe todas as conexões do grafo
    public void exibirGrafo() {
        System.out.println("--- Conexões da Rede Social (Grafo) ---");
        for (String pessoa : grafo.keySet()) {
            System.out.println(pessoa + " é amigo(a) de -> " + grafo.get(pessoa));
        }
    }

    public static void main(String[] args) {
        ExemploGrafo redeSocial = new ExemploGrafo();

        // 1. Criando conexões (arestas) entre os vértices (usuários)
        redeSocial.adicionarAresta("Alice", "Bob");
        redeSocial.adicionarAresta("Alice", "Carlos");
        redeSocial.adicionarAresta("Bob", "Daniel");
        redeSocial.adicionarAresta("Carlos", "Daniel");
        redeSocial.adicionarAresta("Carlos", "Eduardo");

        // 2. Exibindo a estrutura em rede
        redeSocial.exibirGrafo();

        // 3. Consultando os vizinhos (amigos diretos) de um nó específico
        String usuario = "Carlos";
        System.out.println("\nAmigos diretos de " + usuario + ": " + redeSocial.grafo.get(usuario));
    }
}
