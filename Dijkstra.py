INF = float('inf')

def bellman_ford(graph, source):
    n = len(graph)
    dist = [INF] * n
    dist[source] = 0
    
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != INF and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    
    # Check for negative cycles
    for u in range(n):
        for v in range(n):
            if graph[u][v] != INF and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                return None  # Negative cycle detected
    
    return dist
