def dfs(adj_matrix, start):
    visited = [False] * len(adj_matrix)  # Mark all vertices as not visited
    stack = [start]  # Initialize the stack with the starting vertex

    while stack:
        vertex = stack.pop()  # Pop the last vertex from the stack

        if not visited[vertex]:  # If the vertex is not visited
            visited[vertex] = True  # Mark it as visited
            print(vertex)  # Print the vertex

            # Add all adjacent vertices to the stack
            for i in range(len(adj_matrix[vertex])):
                if adj_matrix[vertex][i] == 1 and not visited[i]:
                    stack.append(i)
