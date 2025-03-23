class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def linked_list_lookup(head, element_number):
    current = head
    count = 0

    while count < element_number and current is not None:
        current = current.next
        count += 1

    return current

# Crear una lista enlazada con 5 elementos
head = LinkedListNode(1)
second = LinkedListNode(2)
third = LinkedListNode(3)
fourth = LinkedListNode(4)
fifth = LinkedListNode(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Buscar el nodo en la posición 2 (el tercer elemento, ya que empezamos desde 0)
position = 2
result = linked_list_lookup(head, position)

if result is not None:
    print(f"El valor en la posición {position} es: {result.value}")
else:
    print(f"No se encontró un nodo en la posición {position}.")