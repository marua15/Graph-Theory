import heapq

def prim(graph):
    # Select a random starting vertex
    start_vertex = next(iter(graph))
    visited = set([start_vertex])
    minimum_spanning_tree = []
    edges = [
        (cost, start_vertex, next_vertex)
        for next_vertex, cost in graph[start_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, current_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex, next_vertex, cost))

            for neighbor, edge_cost in graph[next_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_cost, next_vertex, neighbor))

    return minimum_spanning_tree