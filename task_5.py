from collections import deque

import matplotlib.pyplot as plt

from task_4 import build_heap_tree, draw_tree


def dfs(root):
    if root is None:
        return []

    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        # Правий вузол додаємо першим, щоб лівий вийшов зі стека раніше.
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return order


def bfs(root):
    if root is None:
        return []

    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return order


def show_traversals():
    values = [0, 1, 2, 3, 4, 5, 6]
    dfs_root = build_heap_tree(values)
    bfs_root = build_heap_tree(values)
    dfs_order = dfs(dfs_root)
    bfs_order = bfs(bfs_root)
    print('DFS:', [node.value for node in dfs_order])
    print('BFS:', [node.value for node in bfs_order])

    for node in dfs_order + bfs_order:
        node.color = '#e5e7eb'

    figure, axes = plt.subplots(1, 2, figsize=(11, 4))
    total = len(dfs_order)
    for step in range(total):
        if not plt.fignum_exists(figure.number):
            return

        # RGB-складові зростають, тому відтінок стає світлішим.
        shade = 50 + 160 * step // max(1, total - 1)
        color = f'#{shade // 2:02x}{shade:02x}{shade + 35:02x}'
        dfs_order[step].color = color
        bfs_order[step].color = color

        axes[0].clear()
        axes[1].clear()
        draw_tree(dfs_root, axes[0], f'DFS — крок {step + 1} із {total}')
        draw_tree(bfs_root, axes[1], f'BFS — крок {step + 1} із {total}')
        figure.tight_layout()
        plt.pause(0.6)

    plt.show()


if __name__ == '__main__':
    show_traversals()
