import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф вручную
G = nx.Graph()
# Добавляем вершины и ребра
G.add_edges_from([
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 1), # Кольцо
    (1, 3), (2, 4)                          # Дополнительные связи
])

# Вычисляем центральность в собственных векторах
eigenvector_centrality = nx.eigenvector_centrality(G)

# Выводим центральность каждой вершины
print("Центральность в собственных векторах для каждой вершины:")
for node, centrality in eigenvector_centrality.items():
    print(f"Вершина {node}: {centrality:.4f}")

# Визуализация графа
pos = nx.spring_layout(G)  # Расположение вершин
plt.figure(figsize=(8, 6))
nx.draw(
    G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=15, edge_color='gray'
)
# Добавляем метки с центральностями
labels = {node: f"{centrality:.2f}" for node, centrality in eigenvector_centrality.items()}
nx.draw_networkx_labels(G, pos, labels=labels, font_color='red')

plt.title("Граф с метками центральности в собственных векторах", fontsize=16)
plt.show()
