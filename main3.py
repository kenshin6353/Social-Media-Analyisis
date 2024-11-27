import networkx as nx
import matplotlib.pyplot as plt

# Входные параметры: количество вершин и вероятность появления ребра
n = 100  # Количество вершин
p = 0.05  # Вероятность появления ребра между двумя вершинами

# Генерация графа в модели Эрдёша-Реньи
G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины в графе
average_degree_empirical = sum(dict(G.degree()).values()) / n

# Теоретическое значение средней степени вершины
average_degree_theoretical = n * p

# Вывод результатов
print(f"Эмпирическое значение средней степени вершины: {average_degree_empirical:.4f}")
print(f"Теоретическое значение средней степени вершины: {average_degree_theoretical:.4f}")

# Визуализация графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Расположение вершин
nx.draw(
    G, pos, with_labels=True, node_size=300, node_color='skyblue', edge_color='gray'
)
plt.title("Граф модели Эрдёша-Реньи", fontsize=16)
plt.show()
