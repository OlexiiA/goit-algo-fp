import matplotlib.pyplot as plt


def draw_pythagoras_tree(axis, x, y, dx, dy, level):
    # (dx, dy) задає напрямок і довжину нижньої сторони квадрата.
    left_x = x - dy
    left_y = y + dx
    right_x = left_x + dx
    right_y = left_y + dy

    axis.fill(
        [x, x + dx, right_x, left_x],
        [y, y + dy, right_y, left_y],
        color='seagreen',
        edgecolor='white',
        linewidth=0.5,
    )

    if level == 0:
        return

    # Дві нові основи йдуть від кутів квадрата до вершини трикутника.
    peak_x = left_x + (dx - dy) / 2
    peak_y = left_y + (dy + dx) / 2
    draw_pythagoras_tree(axis, left_x, left_y, peak_x - left_x, peak_y - left_y, level - 1)
    draw_pythagoras_tree(axis, peak_x, peak_y, right_x - peak_x, right_y - peak_y, level - 1)


def main():
    answer = input('Вкажіть рівень рекурсії від 0 до 9 (Enter для 5): ')
    try:
        level = int(answer) if answer else 5
    except ValueError:
        print('Введіть ціле число від 0 до 9.')
        return

    if level < 0 or level > 9:
        print('Введіть ціле число від 0 до 9.')
        return

    _, axis = plt.subplots(figsize=(8, 6))
    draw_pythagoras_tree(axis, 0, 0, 1, 0, level)
    axis.set_aspect('equal')
    axis.set_title(f'Дерево Піфагора, рівень {level}')
    axis.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
