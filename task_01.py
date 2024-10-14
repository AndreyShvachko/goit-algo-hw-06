import networkx as nx
import matplotlib.pyplot as plt

# Створення графу.
G = nx.Graph()

# Додавання вершин (станцій).
stations = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(stations)

# Додавання ребер (маршрутів між станціями).
routes = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('C', 'F')]
G.add_edges_from(routes)

# Візуалізація графу.
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз графу.
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступені вершин: {degrees}")
print(f"Середній ступінь: {average_degree:.2f}")