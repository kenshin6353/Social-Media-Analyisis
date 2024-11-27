def read_graph_from_file(filename):
    """
    Reads an adjacency matrix from a file.
    :param filename: The name of the file containing the adjacency matrix.
    :return: A 2D list representing the graph.
    """
    with open(filename, 'r') as file:
        graph = []
        for line in file:
            graph.append(list(map(int, line.split())))
    return graph

def dijkstra(graph, start_vertex):
    """
    Implementation of Dijkstra's algorithm without external libraries.
    :param graph: Adjacency matrix of the graph.
    :param start_vertex: The starting vertex (index of the vertex).
    :return: A list of shortest distances from the start vertex to all other vertices.
    """
    n = len(graph)  # Number of vertices in the graph
    distances = [float('inf')] * n  # Initialize distances to all vertices as infinity
    distances[start_vertex] = 0  # Distance to the start vertex is 0
    visited = [False] * n  # Track whether each vertex has been visited

    for _ in range(n):
        # Find the unvisited vertex with the smallest distance
        min_distance = float('inf')
        min_vertex = -1
        for vertex in range(n):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex == -1:  # All reachable vertices have been visited
            break

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update distances to neighboring vertices
        for neighbor in range(n):
            if graph[min_vertex][neighbor] > 0 and not visited[neighbor]:  # If there's an edge
                new_distance = distances[min_vertex] + graph[min_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

graph = read_graph_from_file("graph.txt")

all_distances = []
for start_vertex in range(len(graph)):
    all_distances.append(dijkstra(graph, start_vertex))

print("Shortest distances between all pairs of vertices:")
for i, distances in enumerate(all_distances):
    print(f"From vertex {i}:")
    for j, distance in enumerate(distances):
        print(f"Vertex {j}: {distance}")
    print()
