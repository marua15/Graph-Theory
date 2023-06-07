import networkx as nx

def prim_mst(graph):
    # Create a new graph for the minimum spanning tree
    mst = nx.Graph()

    # Choose an arbitrary starting node
    start_node = list(graph.nodes())[0]

    # Initialize a set to keep track of visited nodes
    visited = {start_node}

    # Condition that checks whether the length of a list called "visited" 
    # is less than the length of another list called "graph.nodes()". 
    while len(visited) < len(graph.nodes()):
        # Find the minimum weight edge from visited nodes to unvisited nodes
        min_edge = None
        min_weight = float('inf')

        for u in visited:
            for v in graph.neighbors(u):
                if v not in visited:
                    weight = graph[u][v]['weight']
                    if weight < min_weight:
                        min_edge = (u, v)
                        min_weight = weight

        # Add the minimum weight edge to the minimum spanning tree
        if min_edge is not None:
            u, v = min_edge
            mst.add_edge(u, v, weight=min_weight)
            visited.add(v)

    return mst