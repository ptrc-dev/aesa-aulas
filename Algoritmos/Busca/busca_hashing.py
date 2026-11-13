"""
ALGORITMO DE BUSCA: BUSCA POR HASHING (TABELA HASH)
- Requisito: Função Hash para transformar a chave em um índice
- Complexidade: O(1) no caso médio
"""

from typing import Any, Optional


class TabelaHash:
    def __init__(self, tamanho: int = 5):
        self.tamanho = tamanho
        # Cria os baldes (buckets) vazios para guardar os pares (chave, valor)
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave: Any) -> int:
        """Calcula o índice direto usando o operador de resto (%)"""
        return hash(chave) % self.tamanho

    def inserir(self, chave: Any, valor: Any) -> None:
        """Insere ou atualiza um valor associado a uma chave"""
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        # Se a chave já existe no balde, apenas atualiza o valor
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)
                return

        # Se não existe, adiciona no balde (trata colisões)
        bucket.append((chave, valor))

    def buscar(self, chave: Any) -> Optional[Any]:
        """Calcula o hash e vai direto no índice onde o valor deve estar: O(1)"""
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        for k, v in bucket:
            if k == chave:
                return v

        return None  # Chave não encontrada


# -----------------------------------------------------------------------------
# TESTE SIMPLES
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    tabela = TabelaHash(tamanho=5)

    # Inserindo dados
    tabela.inserir("ana", "Nota 10")
    tabela.inserir("carlos", "Nota 8")
    tabela.inserir("pedro", "Nota 9")

    print("--- Busca Direta O(1) ---")
    print(f"Nota da 'ana': {tabela.buscar('ana')}")
    print(f"Nota do 'carlos': {tabela.buscar('carlos')}")
    print(f"Nota do 'lucas': {tabela.buscar('lucas')} (não cadastrado)")
