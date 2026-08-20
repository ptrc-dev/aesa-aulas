package org.aesa;

import java.util.Arrays;

public class ArrayClasseAuxiliar {
    static void main() {
        // 4. Usando a classe auxiliar
        // O java possui uma classe auxiliar chamada Arrays que oferece métodos úteis para manipular arrays

        int[] notas = {8, 5, 10, 3, 7};

        // Imprimindo o array todo de uma vez (sem precisar de um loop)
        System.out.println(Arrays.toString(notas));

        // Ordenando o array em ordem crescente
        Arrays.sort(notas);
        System.out.println(Arrays.toString(notas));
    }
}