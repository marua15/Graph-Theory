import sys

def prim(graph):
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [None] * num_vertices
    key[0] = 0
    mst_set = [False] * num_vertices

    for _ in range(num_vertices):
        min_key = sys.maxsize
        min_index = -1

        for v in range(num_vertices):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        mst_set[min_index] = True

        for v in range(num_vertices):
            if (
                graph[min_index][v] != 0
                and not mst_set[v]
                and graph[min_index][v] < key[v]
            ):
                key[v] = graph[min_index][v]
                parent[v] = min_index

    return parent

# # Printing the minimum spanning tree edges
# print("Minimum Spanning Tree Edges:")
# for i in range(1, len(graph)):
#     print(f"{mst_parent[i]} - {i}")