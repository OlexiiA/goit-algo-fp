items = {
    'pizza': {'cost': 50, 'calories': 300},
    'hamburger': {'cost': 40, 'calories': 250},
    'hot-dog': {'cost': 30, 'calories': 200},
    'pepsi': {'cost': 10, 'calories': 100},
    'cola': {'cost': 15, 'calories': 220},
    'potato': {'cost': 25, 'calories': 350},
}


def greedy_algorithm(items, budget):
    def calories_per_cost(name):
        return items[name]['calories'] / items[name]['cost']

    names = sorted(items, key=calories_per_cost, reverse=True)
    selected = []
    for name in names:
        cost = items[name]['cost']
        if cost <= budget:
            selected.append(name)
            budget -= cost
    return selected


def dynamic_programming(items, budget):
    names = list(items)
    # table[i][money] — максимум калорій для перших i страв і бюджету money.
    table = [[0] * (budget + 1) for _ in range(len(names) + 1)]

    for i in range(1, len(names) + 1):
        food = items[names[i - 1]]
        cost = food['cost']
        for money in range(budget + 1):
            table[i][money] = table[i - 1][money]
            if cost <= money:
                with_food = food['calories'] + table[i - 1][money - cost]
                if with_food > table[i][money]:
                    table[i][money] = with_food

    selected = []
    money = budget
    for i in range(len(names), 0, -1):
        if table[i][money] != table[i - 1][money]:
            name = names[i - 1]
            selected.append(name)
            money -= items[name]['cost']

    selected.reverse()
    return selected


def print_result(title, selected):
    total_cost = 0
    total_calories = 0
    for name in selected:
        total_cost += items[name]['cost']
        total_calories += items[name]['calories']
    print(title, selected)
    print(f'Вартість {total_cost}, калорійність {total_calories}')


if __name__ == '__main__':
    budget = 100
    print('Бюджет:', budget)
    print_result('Жадібний алгоритм:', greedy_algorithm(items, budget))
    print_result('Динамічне програмування:', dynamic_programming(items, budget))
