import networkx as nx

def kruskal_mst(G):
    # Create a minimum spanning tree graph
    mst = nx.Graph()
    
    # Sort the edges of the input graph based on their weights
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    
    # Add nodes to the minimum spanning tree
    for node in G.nodes():
        mst.add_node(node)
    
    # Iterate over the sorted edges and add them to the minimum spanning tree if they don't create a cycle
    for edge in sorted_edges:
        u, v, attr = edge
        if nx.find_cycle(mst, source=u) is None:
            mst.add_edge(u, v, **attr)
    
    return mst