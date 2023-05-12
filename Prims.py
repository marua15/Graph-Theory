import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        for v in range(self.vertices):
            if key[v] < min_value and mst_set[v] == False:
                min_value = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.vertices
        parent = [None] * self.vertices
        key[0] = 0
        mst_set = [False] * self.vertices
        parent[0] = -1

        for _ in range(self.vertices):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)
