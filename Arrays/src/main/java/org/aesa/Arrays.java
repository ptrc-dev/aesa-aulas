package org.aesa;

public class Arrays {
    static void main() {
        //1 - Declarando e Inicializando Arrays
        // Opção A: Criando e já preenchendo com valores

        String[] frutas = {"Maçã", "Banana", "Laranja", "Uva"};
        int[] numerosSorteados = {4, 8, 15, 16, 23, 42};

        // Opção B: Criando um array vazio com tamanho fixo (ex: 5 posições)
        // Por padrão, arrays de int começam com zeros.
        int[] pontuacoes = new int[5];

        //2 - Acessando e Modificando Elementos

        String[] carros = {"Fusca", "Gol", "Palio"};

        // Acessando o primeiro elemento
        System.out.println(carros[0]); // Saída: Fusca

        // Modificando o valor de um elemento
        carros[1] = "Civic";
        System.out.println(carros[1]); // Saída: Civic

        // Descobrindo o tamanho total do array
        int tamanho = carros.length;
        System.out.println("Quantidade de carros: " + tamanho); // Saída: 3

        //3 - Percorrendo um Array (Loops)

        String[] nomes = {"Ana", "Carlos", "Beatriz"};

        // Usando o for tradicional (útil quando você precisa saber o índice)
        for (int i = 0; i < nomes.length; i++) {
            System.out.println("Posição " + i + ": " + nomes[i]);
        }

        // Usando o for-each (mais limpo e direto)
        for (String nome : nomes) {
            System.out.println("Nome: " + nome);
        }
    }
}