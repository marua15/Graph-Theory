import sys

def bellman_ford(graph, start):
    num_vertices = len(graph)
    distance = {v: sys.maxsize for v in graph}
    distance[start] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        for u in graph:
            for v in graph[u]:
                weight = graph[u][v]
                if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Check for negative cycles
    for u in graph:
        for v in graph[u]:
            weight = graph[u][v]
            if distance[u] != sys.maxsize and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance

# Example usage
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3},
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)

# Print the distances from the start vertex to all other vertices
for v in distances:
    print(f"Distance from vertex {start_vertex} to vertex {v} is {distances[v]}")
