def warshall(graph):
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    distances = {node: {v: float('inf') for v in nodes} for node in nodes}
    
    for node in nodes:
        distances[node][node] = 0
    
    for node in graph:
        for neighbor, weight in graph[node].items():
            distances[node][neighbor] = weight
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return distances