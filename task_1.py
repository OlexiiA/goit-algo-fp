class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_list(values):
    start = Node(None)
    tail = start
    for value in values:
        tail.next = Node(value)
        tail = tail.next
    return start.next


def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def insertion_sort(head):
    start = Node(None)
    current = head
    while current is not None:
        next_node = current.next
        # Шукаємо місце для вузла у вже відсортованій частині.
        position = start
        while position.next is not None and position.next.value <= current.value:
            position = position.next
        current.next = position.next
        position.next = current
        current = next_node
    return start.next


def merge_sorted_lists(first, second):
    start = Node(None)
    tail = start
    while first is not None and second is not None:
        if first.value <= second.value:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next

    if first is not None:
        tail.next = first
    else:
        tail.next = second
    return start.next


def print_list(head):
    values = []
    while head is not None:
        values.append(str(head.value))
        head = head.next
    print(' -> '.join(values))


if __name__ == '__main__':
    first = create_list([4, 2, 7, 1])
    print('Початковий список')
    print_list(first)

    first = reverse_list(first)
    print('Після реверсу')
    print_list(first)

    first = insertion_sort(first)
    print('Після сортування')
    print_list(first)

    second = create_list([0, 3, 8])
    print('Об’єднання зі списком 0 -> 3 -> 8')
    print_list(merge_sorted_lists(first, second))
