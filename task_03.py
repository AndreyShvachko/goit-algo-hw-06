import heapq

# Реалізація алгоритму Дейкстри
def dijkstra_custom(graph, start):
    # Ініціалізація: відстані до всіх вершин є нескінченними, окрім стартової
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Черга з пріоритетами для вершин, які ще треба опрацювати
    priority_queue = [(0, start)]
    
    # Для зберігання попередніх вершин, щоб потім відновити шлях
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Якщо знайдено коротший шлях, продовжуємо пошук
        if current_distance > distances[current_node]:
            continue
        
        # Оглядаємо сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда, оновлюємо дані
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

# Відновлення шляху з попередніх вершин
def reconstruct_path(previous_nodes, start, target):
    path = []
    current_node = target
    
    # Рухаємося назад від кінцевої вершини до стартової
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []

# Створюємо граф з вагами (аналогічно попередньому прикладу)
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 4},
    'C': {'A': 2, 'D': 1, 'F': 5},
    'D': {'B': 4, 'C': 1, 'E': 2},
    'E': {'D': 2, 'F': 3},
    'F': {'C': 5, 'E': 3}
}

# Запускаємо алгоритм Дейкстри
start_node = 'A'
target_node = 'F'
distances, previous_nodes = dijkstra_custom(graph, start_node)

# Виведення результатів
print(f"Найкоротші відстані від вершини {start_node}: {distances}")
path = reconstruct_path(previous_nodes, start_node, target_node)
print(f"Найкоротший шлях від {start_node} до {target_node}: {path}")
print(f"Довжина найкоротшого шляху: {distances[target_node]}")

