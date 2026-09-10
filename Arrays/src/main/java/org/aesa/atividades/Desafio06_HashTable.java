package org.aesa.atividades;

import java.util.HashMap;
import java.util.Map;

/**
 * DESAFIO 06 - TABELA HASH (HASHMAP / CHAVE-VALOR)
 * 
 * Objetivo: Praticar a manipulação de tabelas hash (Map/HashMap), inserção por chave,
 * busca O(1), verificação de existência, atualização, remoção e iteração de pares.
 * 
 * Cenário: Catálogo de Preços de Produtos em uma Loja de Informática (Código SKU -> Preço).
 * 
 * Instruções:
 * 1. Crie uma tabela hash usando Map<String, Double> chamada catalogoProdutos = new HashMap<>().
 * 2. Adicione 5 produtos ao catálogo associando o código/SKU (Chave) ao seu Preço em reais (Valor):
 *    - "NOTE-01" -> 3500.00
 *    - "TECL-02" -> 250.00
 *    - "MOUS-03" -> 120.00
 *    - "MONI-04" -> 1100.00
 *    - "HEAD-05" -> 320.00
 * 3. Consulte e exiba o preço do produto "NOTE-01" utilizando o método get().
 * 4. Verifique se o produto com código "WEBC-06" está cadastrado utilizando containsKey().
 * 5. Atualize o valor do teclado ("TECL-02") aplicando um desconto promocional para 199.90.
 * 6. Remova o produto "MOUS-03" do catálogo pois saiu de linha (método remove()).
 * 7. Exiba a quantidade total de produtos cadastrados atualmente (size()).
 * 8. Percorra todo o catálogo utilizando entrySet() e exiba cada par Código -> Preço formatado.
 */
public class Desafio06_HashTable {

    public static void main(String[] args) {
        // TODO: Crie a tabela hash usando Map<String, Double> e HashMap<>
        Map<String, Double> catalogoProdutos = new HashMap<>();

        // TODO: Adicione 5 produtos com seus respectivos códigos (chave) e preços (valor) usando put()
        catalogoProdutos.put("NOTE-01", 3500.00);
        catalogoProdutos.put("TECL-02", 250.00);
        catalogoProdutos.put("MOUS-03", 120.00);
        catalogoProdutos.put("MONI-04", 1100.00);
        catalogoProdutos.put("HEAD-05", 320.00);

        // TODO: Consulte o preço de um produto específico com get()
        System.out.println("Preço do Notebook (NOTE-01): R$ " + catalogoProdutos.get("NOTE-01"));

        // TODO: Verifique se determinado produto está cadastrado com containsKey()
        String codigoConsulta = "WEBC-06";
        System.out.println("O produto " + codigoConsulta + " está cadastrado? " + catalogoProdutos.containsKey(codigoConsulta));

        // TODO: Atualize o preço de um produto existente (mesma chave, novo valor)
        catalogoProdutos.put("TECL-02", 199.90);
        System.out.println("Novo preço do Teclado (TECL-02): R$ " + catalogoProdutos.get("TECL-02"));

        // TODO: Remova um produto descontinuado usando remove()
        catalogoProdutos.remove("MOUS-03");
        System.out.println("Produto MOUS-03 removido do catálogo.");

        // TODO: Exiba o total de produtos cadastrados (size())
        System.out.println("Total de produtos no catálogo: " + catalogoProdutos.size());

        // TODO: Percorra todos os produtos com entrySet() e imprima formatado
        System.out.println("\n--- Catálogo Atualizado de Produtos (Código -> Preço) ---");
        for (Map.Entry<String, Double> item : catalogoProdutos.entrySet()) {
            System.out.println("Código: " + item.getKey() + " | Preço: R$ " + String.format("%.2f", item.getValue()));
        }
    }
}
