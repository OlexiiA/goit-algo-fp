import random


def simulate_rolls(rolls):
    counts = {total: 0 for total in range(2, 13)}
    for _ in range(rolls):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        counts[first + second] += 1
    return counts


def theoretical_counts():
    counts = {total: 0 for total in range(2, 13)}
    for first in range(1, 7):
        for second in range(1, 7):
            counts[first + second] += 1
    return counts


if __name__ == '__main__':
    rolls = 100_000
    random.seed(42)
    counts = simulate_rolls(rolls)
    possible_pairs = theoretical_counts()

    print(f'Кількість кидків: {rolls}')
    print('Сума | Кількість | Монте-Карло | Теорія')
    for total in range(2, 13):
        simulated = counts[total] / rolls
        theoretical = possible_pairs[total] / 36
        print(f'{total:4} | {counts[total]:9} | {simulated:11.2%} | {theoretical:6.2%}')
