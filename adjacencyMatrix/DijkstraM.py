import sys

def dijkstra(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    distance[start] = 0

    for _ in range(num_vertices):
        min_dist = sys.maxsize
        min_index = -1

        # Find the vertex with the minimum distance
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v

        # Mark the selected vertex as visited
        visited[min_index] = True

        # Update distances for the neighboring vertices
        for v in range(num_vertices):
            if (
                not visited[v]
                and graph[min_index][v] != 0
                and distance[min_index] != sys.maxsize
                and distance[min_index] + graph[min_index][v] < distance[v]
            ):
                distance[v] = distance[min_index] + graph[min_index][v]

    return distance

# # Example usage
# adjacency_matrix = [
#     [0, 4, 0, 0, 0, 0, 0, 8, 0],
#     [4, 0, 8, 0, 0, 0, 0, 11, 0],
#     [0, 8, 0, 7, 0, 4, 0, 0, 2],
#     [0, 0, 7, 0, 9, 14, 0, 0, 0],
#     [0, 0, 0, 9, 0, 10, 0, 0, 0],
#     [0, 0, 4, 14, 10, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 1, 6],
#     [8, 11, 0, 0, 0, 0, 1, 0, 7],
#     [0, 0, 2, 0, 0, 0, 6, 7, 0],
# ]

# start_vertex = 0
# distances = dijkstra(adjacency_matrix, start_vertex)

# # Print the distances from the start vertex to all other vertices
# for i, distance in enumerate(distances):
#     print(f"Distance from vertex {start_vertex} to vertex {i} is {distance}")
