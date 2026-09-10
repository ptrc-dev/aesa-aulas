package org.aesa;

import java.util.Arrays;

/**
 * EXEMPLO - BUSCA BINÁRIA VS BUSCA LINEAR
 * 
 * Por que precisamos entender Estruturas de Dados?
 * 
 * Porque algoritmos eficientes exigem que os dados estejam estruturados
 * de forma adequada na memória. Se os dados estiverem em um array ordenado,
 * podemos usar a Busca Binária para reduzir o tempo de busca de O(n) para O(log n).
 */
public class ExemploBuscaBinaria {

    // 1. Busca Linear (Estrutura Sequencial não ordenada ou sem acesso inteligente)
    // Complexidade: O(n) - No pior caso, precisa percorrer todo o array
    public static int buscaLinear(int[] array, int alvo) {
        int comparacoes = 0;
        for (int i = 0; i < array.length; i++) {
            comparacoes++;
            if (array[i] == alvo) {
                System.out.println("  [Busca Linear] Encontrado no índice " + i + " após " + comparacoes + " comparações.");
                return i;
            }
        }
        System.out.println("  [Busca Linear] Não encontrado após " + comparacoes + " comparações.");
        return -1;
    }

    // 2. Busca Binária (Estrutura com Acesso Indexado O(1) + Dados Ordenados)
    // Complexidade: O(log n) - A cada passo, corta metade do problema
    public static int buscaBinaria(int[] array, int alvo) {
        int inicio = 0;
        int fim = array.length - 1;
        int comparacoes = 0;

        while (inicio <= fim) {
            comparacoes++;
            // Calcula o ponto médio para dividir o espaço de busca ao meio
            int meio = inicio + (fim - inicio) / 2;

            if (array[meio] == alvo) {
                System.out.println("  [Busca Binária] Encontrado no índice " + meio + " após APENAS " + comparacoes + " comparações!");
                return meio;
            }

            if (array[meio] < alvo) {
                // Se o valor do meio é menor, o alvo só pode estar na metade direita
                inicio = meio + 1;
            } else {
                // Se o valor do meio é maior, o alvo só pode estar na metade esquerda
                fim = meio - 1;
            }
        }

        System.out.println("  [Busca Binária] Não encontrado após " + comparacoes + " comparações.");
        return -1;
    }

    public static void main(String[] args) {
        System.out.println("===================================================================");
        System.out.println("  POR QUE ENTENDER ESTRUTURAS DE DADOS? BUSCA LINEAR VS BINÁRIA    ");
        System.out.println("===================================================================\n");

        // Criando um array ordenado de 1.000.000 de elementos (1 a 1.000.000)
        int tamanho = 1_000_000;
        int[] dados = new int[tamanho];
        for (int i = 0; i < tamanho; i++) {
            dados[i] = i + 1;
        }

        // Elemento que queremos encontrar (o último elemento - Pior Caso da busca linear)
        int alvoPiorCaso = 1_000_000;
        System.out.println("Cenário: Procurando o número " + alvoPiorCaso + " em uma coleção de " + tamanho + " elementos:\n");

        long tempoInicio = System.nanoTime();
        buscaLinear(dados, alvoPiorCaso);
        long tempoLinear = System.nanoTime() - tempoInicio;

        tempoInicio = System.nanoTime();
        buscaBinaria(dados, alvoPiorCaso);
        long tempoBinario = System.nanoTime() - tempoInicio;

        System.out.println("\nTempo Busca Linear:  " + (tempoLinear / 1_000_000.0) + " ms");
        System.out.println("Tempo Busca Binária: " + (tempoBinario / 1_000_000.0) + " ms");

        // Uso do método nativo da classe auxiliar Arrays do Java
        System.out.println("\n--- Usando o método nativo do Java: Arrays.binarySearch() ---");
        int indiceNativo = Arrays.binarySearch(dados, alvoPiorCaso);
        System.out.println("Índice retornado pelo Java: " + indiceNativo);

        System.out.println("\n-------------------------------------------------------------------");
        System.out.println("  CONCLUSÃO PEDAGÓGICA:");
        System.out.println("  1. Para 1 milhão de itens:");
        System.out.println("     - Busca Linear: 1.000.000 de passos.");
        System.out.println("     - Busca Binária: no máximo 20 passos (log2(1.000.000) ≈ 20).");
        System.out.println("  2. Para 1 bilhão de itens:");
        System.out.println("     - Busca Linear: 1.000.000.000 de passos.");
        System.out.println("     - Busca Binária: no máximo 30 passos!");
        System.out.println("  3. MAS A BUSCA BINÁRIA SÓ FUNCIONA PORQUE OS DADOS ESTÃO");
        System.out.println("     ORGANIZADOS (ESTRUTURADOS) EM ORDEM E COM ACESSO DIRETO.");
        System.out.println("     Essa é a razão pela qual estudamos Estruturas de Dados!");
        System.out.println("-------------------------------------------------------------------");
    }
}
