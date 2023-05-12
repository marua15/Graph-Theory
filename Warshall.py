INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    
    # initialize distance matrix and path matrix
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(num_vertices)] for i in range(num_vertices)]
    path = [[-1 if i == j or graph[i][j] == 0 else i for j in range(num_vertices)] for i in range(num_vertices)]
    
    # apply the algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
    
    return dist, path
