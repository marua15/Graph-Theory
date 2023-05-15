import sys

def bellman_ford(adj_matrix, start):
    num_vertices = len(adj_matrix)
    distance = [sys.maxsize] * num_vertices
    distance[start] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = adj_matrix[u][v]
                if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Check for negative cycles
    for u in range(num_vertices):
        for v in range(num_vertices):
            weight = adj_matrix[u][v]
            if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance

# # Example usage
# adjacency_matrix = [
#     [0, -1, 4, 0, 0],
#     [0, 0, 3, 2, 2],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 5],
#     [0, 0, 0, -3, 0],
# ]

# start_vertex = 0
# distances = bellman_ford(adjacency_matrix, start_vertex)

# # Print the distances from the start vertex to all other vertices
# for i, distance in enumerate(distances):
#     print(f"Distance from vertex {start_vertex} to vertex {i} is {distance}")
