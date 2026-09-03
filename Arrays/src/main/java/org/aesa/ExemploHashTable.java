package org.aesa;

import java.util.HashMap;
import java.util.Map;

public class ExemploHashTable {
    public static void main(String[] args) {
        // As Tabelas Hash armazenam dados no formato Chave -> Valor.
        // No Java, a classe mais comum e moderna é o HashMap.
        // Ela calcula um código "hash" da chave para acessar o valor diretamente em O(1).

        // Criando uma tabela hash para associar o CPF (Chave) ao Nome do Aluno (Valor)
        Map<String, String> alunosPorCpf = new HashMap<>();

        // 1. Inserindo pares chave-valor com put()
        alunosPorCpf.put("111.222.333-44", "Lucas Silva");
        alunosPorCpf.put("222.333.444-55", "Mariana Souza");
        alunosPorCpf.put("333.444.555-66", "Rafael Oliveira");

        // 2. Buscando um valor diretamente pela chave com get()
        String aluno = alunosPorCpf.get("222.333.444-55");
        System.out.println("Aluno encontrado pelo CPF: " + aluno);
        // Saída: Mariana Souza

        // 3. Verificando se uma chave ou valor existe
        boolean temCpf = alunosPorCpf.containsKey("111.222.333-44");
        System.out.println("CPF 111.222.333-44 está cadastrado? " + temCpf);

        // 4. Atualizando um valor (basta fazer put com a mesma chave)
        alunosPorCpf.put("111.222.333-44", "Lucas Silva Atualizado");

        // 5. Removendo um elemento pela chave
        alunosPorCpf.remove("333.444.555-66");

        // 6. Percorrendo todos os pares da Tabela Hash
        System.out.println("\n--- Lista Completa de Alunos (Chave : Valor) ---");
        for (Map.Entry<String, String> registro : alunosPorCpf.entrySet()) {
            System.out.println("CPF: " + registro.getKey() + " -> Nome: " + registro.getValue());
        }
    }
}
