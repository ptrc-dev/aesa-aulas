"""
MERGE SORT COM LISTA ENCADEADA (PONTEIROS .next)
Exemplo simples para os valores: 3, 1, 9, 7
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def encontrar_meio(head):
    """Usa ponteiros lento (1 passo) e rápido (2 passos) para achar o meio."""
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):
    """Intercala duas listas encadeadas já ordenadas."""
    dummy = Node()  # Nó temporário apenas para marcar o início
    atual = dummy

    while left and right:
        if left.val <= right.val:
            atual.next = left
            left = left.next
        else:
            atual.next = right
            right = right.next
        atual = atual.next

    # Conecta o restante que sobrou em um dos lados
    atual.next = left or right
    return dummy.next


def merge_sort(head):
    # Caso base: 0 ou 1 elemento já está ordenado
    if not head or not head.next:
        return head

    # 1. Divisão: encontra o meio e separa em duas listas
    meio = encontrar_meio(head)
    direita = meio.next
    meio.next = None  # Corta a ligação entre a metade esquerda e a direita

    # 2. Recursão: ordena as duas metades
    esquerda_ordenada = merge_sort(head)
    direita_ordenada = merge_sort(direita)

    # 3. Conquista: junta as duas metades em ordem
    return merge(esquerda_ordenada, direita_ordenada)


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

    ordenada = merge_sort(head)

    print("Depois:")
    imprimir_lista(ordenada)

