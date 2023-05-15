import tkinter as tk

def dfs(adj_matrix, start_node):
    n = len(adj_matrix)
    visited = [False] * n
    stack = []

    stack.append(start_node)

    dfs_result = []

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
            dfs_result.append(str(current_node))  # Store the node value as a string

            for neighbor in range(n - 1, -1, -1):  # Iterate in reverse order for consistent ordering
                if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return ' -> '.join(dfs_result)  # Join the node values with ' -> ' delimiter

