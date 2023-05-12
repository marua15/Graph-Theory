def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(graph):
    n = len(graph)
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    result = []

    i = 0
    edges = []
    for u in range(n):
        for v in range(u+1, n):
            if graph[u][v] != 0:
                edges.append((graph[u][v], u, v))

    edges = sorted(edges)

    while i < n-1:
        weight, u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append((u, v, weight))
            union(parent, rank, x, y)

    return result
