def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    num_vertices = len(graph)
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    min_spanning_tree = []

    edge_count = 0
    while edge_count < num_vertices - 1:
        min_weight = float('inf')
        u = -1
        v = -1

        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] < min_weight and find(parent, i) != find(parent, j):
                    min_weight = graph[i][j]
                    u = i
                    v = j

        union(parent, rank, u, v)
        min_spanning_tree.append((u, v, min_weight))
        edge_count += 1

    return min_spanning_tree

# Example graph represented as an adjacency matrix
# graph = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0],
# ]

# # Calling the Kruskal's algorithm function
# mst = kruskal(graph)

# # Printing the minimum spanning tree edges
# print("Minimum Spanning Tree Edges:")
# for u, v, weight in mst:
#     print(f"{u} - {v} : {weight}")
