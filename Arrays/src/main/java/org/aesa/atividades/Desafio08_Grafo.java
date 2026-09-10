package org.aesa.atividades;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * DESAFIO 08 - GRAFOS (REDE / LISTA DE ADJACÊNCIA)
 * 
 * Objetivo: Praticar a modelagem de grafos não-lineares em rede, implementando
 * lista de adjacência, adição de vértices/arestas, consulta de vizinhança e verificação de conexões diretas.
 * 
 * Cenário: Malha Aérea de Companhia de Aviação (Cidades e Voos Diretos).
 * 
 * Instruções:
 * 1. Represente o grafo com uma lista de adjacência usando Map<String, List<String>>.
 * 2. Crie o método adicionarAeroporto(String cidade) para cadastrar os vértices.
 * 3. Crie o método adicionarVoo(String origem, String destino) para cadastrar voos bidirecionais (arestas).
 * 4. Cadastre as rotas aéreas entre as seguintes capitais:
 *    - "São Paulo" <-> "Rio de Janeiro"
 *    - "São Paulo" <-> "Brasília"
 *    - "São Paulo" <-> "Curitiba"
 *    - "Rio de Janeiro" <-> "Salvador"
 *    - "Brasília" <-> "Salvador"
 *    - "Brasília" <-> "Manaus"
 * 5. Exiba o mapa completo da malha aérea (todas as cidades e suas rotas).
 * 6. Consulte e liste todos os voos diretos que partem de "São Paulo".
 * 7. Implemente e teste o método temVooDireto(String origem, String destino) verificando:
 *    - Se há voo direto entre "São Paulo" e "Salvador" (deve ser false).
 *    - Se há voo direto entre "Brasília" e "Manaus" (deve ser true).
 * 8. Exiba a quantidade total de voos diretos que saem do aeroporto de "São Paulo".
 */
public class Desafio08_Grafo {

    // TODO: Crie a estrutura do Grafo como Lista de Adjacência
    private Map<String, List<String>> grafo = new HashMap<>();

    // TODO: Implemente a adição de vértice
    public void adicionarAeroporto(String cidade) {
        grafo.putIfAbsent(cidade, new ArrayList<>());
    }

    // TODO: Implemente a adição de aresta bidirecional
    public void adicionarVoo(String origem, String destino) {
        adicionarAeroporto(origem);
        adicionarAeroporto(destino);

        // Evita conexões duplicadas
        if (!grafo.get(origem).contains(destino)) {
            grafo.get(origem).add(destino);
        }
        if (!grafo.get(destino).contains(origem)) {
            grafo.get(destino).add(origem);
        }
    }

    // TODO: Implemente a exibição de todas as conexões
    public void exibirMalhaAerea() {
        System.out.println("--- Malha Aérea Completa (Cidades e Conexões) ---");
        for (Map.Entry<String, List<String>> rota : grafo.entrySet()) {
            System.out.println(rota.getKey() + " conecta-se com -> " + rota.getValue());
        }
    }

    // TODO: Verifique se existe voo direto entre duas cidades
    public boolean temVooDireto(String origem, String destino) {
        if (!grafo.containsKey(origem) || !grafo.containsKey(destino)) {
            return false;
        }
        return grafo.get(origem).contains(destino);
    }

    // TODO: Obtenha a quantidade de voos diretos (grau do vértice)
    public int quantidadeVoosDiretos(String cidade) {
        if (!grafo.containsKey(cidade)) {
            return 0;
        }
        return grafo.get(cidade).size();
    }

    public static void main(String[] args) {
        Desafio08_Grafo malhaAerea = new Desafio08_Grafo();

        // TODO: Cadastre os voos entre as cidades
        malhaAerea.adicionarVoo("São Paulo", "Rio de Janeiro");
        malhaAerea.adicionarVoo("São Paulo", "Brasília");
        malhaAerea.adicionarVoo("São Paulo", "Curitiba");
        malhaAerea.adicionarVoo("Rio de Janeiro", "Salvador");
        malhaAerea.adicionarVoo("Brasília", "Salvador");
        malhaAerea.adicionarVoo("Brasília", "Manaus");

        // TODO: Exiba o grafo completo da malha aérea
        malhaAerea.exibirMalhaAerea();

        // TODO: Consulte os voos que partem de São Paulo
        String aeroportoOrigem = "São Paulo";
        System.out.println("\nVoos diretos saindo de " + aeroportoOrigem + ": " + malhaAerea.grafo.get(aeroportoOrigem));
        System.out.println("Total de conexões diretas de " + aeroportoOrigem + ": " + malhaAerea.quantidadeVoosDiretos(aeroportoOrigem));

        // TODO: Teste se existem voos diretos
        System.out.println("\n--- Verificação de Voos Diretos ---");
        System.out.println("Existe voo direto entre São Paulo e Salvador? " + malhaAerea.temVooDireto("São Paulo", "Salvador"));
        System.out.println("Existe voo direto entre Brasília e Manaus? " + malhaAerea.temVooDireto("Brasília", "Manaus"));
    }
}
