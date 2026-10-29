package org.aesa.atividades;

import java.util.Arrays;

/**
 * DESAFIO 01 - ARRAYS (VETORES) E CLASSE AUXILIAR
 * 
 * Objetivo: Praticar declaração, iteração, cálculo de estatísticas e o uso de Arrays.sort().
 * 
 * Instruções:
 * 1. Declare um array de double com 5 notas de alunos (ex: 7.5, 4.0, 9.2, 5.5, 8.0).
 * 2. Calcule e exiba a média de todas as notas do array.
 * 3. Utilize Arrays.sort() para ordenar as notas em ordem crescente.
 * 4. Exiba a menor nota (primeiro elemento) e a maior nota (último elemento).
 * 5. Exiba o array completo formatado usando Arrays.toString().
 */
public class Desafio01_Arrays {

    public static void main(String[] args) {
        // TODO: Declare e inicialize o array de notas com 5 valores
        double[] notas = {7.5, 4.0, 9.2, 5.5, 8.0};

        // TODO: Obtenha o tamanho total do array
        int quantidadeNotas = notas.length;

        // TODO: Calcule a soma de todas as notas utilizando um loop for ou for-each
        double soma = 0;
        for (double nota : notas) {
            soma += nota;
        }

        double media = soma / quantidadeNotas;
        System.out.println("Média das notas: " + media);

        // TODO: Ordene o array de notas em ordem crescente utilizando a classe auxiliar Arrays
        Arrays.sort(notas);

        // TODO: Imprima o array ordenado usando Arrays.toString()
        System.out.println("Notas ordenadas: " + Arrays.toString(notas));

        // TODO: Imprima a menor e a maior nota com base nas posições do array ordenado
        System.out.println("Menor nota: " + notas[0]);
        System.out.println("Maior nota: " + notas[notas.length - 1]);
    }
}
