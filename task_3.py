import heapq


def dijkstra(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')

    distances[start] = 0
    previous = {}
    heap = [(0, start)]

    while heap:
        distance, vertex = heapq.heappop(heap)
        if distance > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = vertex
                heapq.heappush(heap, (new_distance, neighbor))

    return distances, previous


def get_path(previous, start, end):
    path = [end]
    while end != start:
        if end not in previous:
            return []
        end = previous[end]
        path.append(end)

    path.reverse()
    return path


if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2},
    }
    start = 'A'
    distances, previous = dijkstra(graph, start)
    for vertex in graph:
        path = get_path(previous, start, vertex)
        if path:
            print(f'{vertex}: відстань {distances[vertex]}, шлях {" -> ".join(path)}')
        else:
            print(f'{vertex}: шляху немає')
