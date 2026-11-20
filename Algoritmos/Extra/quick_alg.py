"""
QUICK SORT COM LISTA ENCADEADA (PONTEIROS .next)
Exemplo simples para os valores: 3, 1, 9, 7
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def particionar(head):
    """Escolhe o primeiro nó como pivô e separa o resto em menores e maiores."""
    pivo = head
    menores_dummy = Node()
    maiores_dummy = Node()

    menores = menores_dummy
    maiores = maiores_dummy

    atual = head.next
    while atual:
        if atual.val <= pivo.val:
            menores.next = atual
            menores = menores.next
        else:
            maiores.next = atual
            maiores = maiores.next
        atual = atual.next

    # Encerra o final de cada lista para evitar ciclos nos ponteiros
    menores.next = None
    maiores.next = None
    pivo.next = None

    return menores_dummy.next, pivo, maiores_dummy.next


def concatenar(menores, pivo, maiores):
    """Liga tudo em sequência: menores -> pivô -> maiores."""
    pivo.next = maiores

    if not menores:
        return pivo

    # Vai até o último nó da lista de menores e liga no pivô
    atual = menores
    while atual.next:
        atual = atual.next
    atual.next = pivo

    return menores


def quick_sort(head):
    # Caso base: 0 ou 1 elemento já está ordenado
    if not head or not head.next:
        return head

    # 1. Particionamento: separa em menores, pivô e maiores
    menores, pivo, maiores = particionar(head)

    # 2. Recursão: ordena as duas partições
    menores_ordenados = quick_sort(menores)
    maiores_ordenados = quick_sort(maiores)

    # 3. Conquista: junta tudo (menores -> pivô -> maiores)
    return concatenar(menores_ordenados, pivo, maiores_ordenados)


def imprimir_lista(head):
    valores = []
    atual = head
    while atual:
        valores.append(str(atual.val))
        atual = atual.next
    print(" -> ".join(valores))


# -----------------------------------------------------------------------------
# TESTE COM: 3, 1, 9, 7
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Monta a lista encadeada: 3 -> 1 -> 9 -> 7
    head = Node(3, Node(1, Node(9, Node(7))))

    print("Antes:")
    imprimir_lista(head)

    ordenada = quick_sort(head)

    print("Depois:")
    imprimir_lista(ordenada)

