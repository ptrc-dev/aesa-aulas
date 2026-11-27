"""
BUSCA POR HASHING (TABELA HASH)
Exemplo simples para os valores: 3, 1, 9, 7
"""


class TabelaHash:
    def __init__(self, tamanho=5):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Buckets para tratar colisões

    def _hash(self, chave):
        """Calcula o índice direto usando o resto da divisão."""
        return chave % self.tamanho

    def inserir(self, chave):
        indice = self._hash(chave)
        if chave not in self.tabela[indice]:
            self.tabela[indice].append(chave)

    def buscar(self, chave):
        """Calcula o índice e verifica direto no bucket: O(1) médio."""
        indice = self._hash(chave)
        return chave in self.tabela[indice]


# -----------------------------------------------------------------------------
# TESTE COM: 3, 1, 9, 7
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    tabela = TabelaHash(tamanho=5)

    for num in [3, 1, 9, 7]:
        tabela.inserir(num)

    print("Estrutura dos buckets:", tabela.tabela)
    print(f"\nBuscando 9  -> encontrado? {tabela.buscar(9)}")
    print(f"Buscando 5  -> encontrado? {tabela.buscar(5)}")

