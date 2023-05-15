class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    vertices = set(graph.keys())
    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []
    edges = []

    # Collect all edges in a list
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((weight, vertex, neighbor))

    # Sort the edges in ascending order of weight
    edges.sort()

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            minimum_spanning_tree.append((vertex1, vertex2, weight))

    return minimum_spanning_tree