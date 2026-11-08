import heapq

import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = '#a9d6ef'


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(value) for value in heap]
    for index in range(len(nodes)):
        # Для вузла з індексом i діти мають індекси 2*i + 1 і 2*i + 2.
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(nodes):
            nodes[index].left = nodes[left]
        if right < len(nodes):
            nodes[index].right = nodes[right]
    return nodes[0]


def draw_tree(root, axis, title):
    axis.set_title(title)
    axis.axis('off')
    if root is None:
        return

    stack = [(root, 0, 0, 1)]
    while stack:
        node, x, y, level = stack.pop()
        shift = 1 / 2 ** level
        if node.left is not None:
            axis.plot([x, x - shift], [y, y - 1], color='gray', zorder=1)
            stack.append((node.left, x - shift, y - 1, level + 1))
        if node.right is not None:
            axis.plot([x, x + shift], [y, y - 1], color='gray', zorder=1)
            stack.append((node.right, x + shift, y - 1, level + 1))

        axis.scatter(x, y, s=850, color=node.color, edgecolors='#334155', zorder=2)
        # На темних вузлах використовуємо білий текст.
        text_color = 'white' if int(node.color[3:5], 16) < 130 else 'black'
        axis.text(x, y, str(node.value), ha='center', va='center', color=text_color, zorder=3)

    axis.set_xlim(-1, 1)
    axis.margins(y=0.22)


def visualize_heap(heap):
    root = build_heap_tree(heap)
    _, axis = plt.subplots(figsize=(7, 4))
    draw_tree(root, axis, 'Бінарна мінімальна купа')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    heap = [10, 4, 5, 1, 3, 0, 5]
    heapq.heapify(heap)
    print('Купа у вигляді списку:', heap)
    visualize_heap(heap)
