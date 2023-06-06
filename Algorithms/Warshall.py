def floyd_warshall(graph):
    dist = {}
    for u in graph:
        dist[u] = {}
        for v in graph:
            dist[u][v] = float('inf')
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]

    for k in graph:
        for i in graph:
            for j in graph:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
