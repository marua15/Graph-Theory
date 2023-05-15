from queue import Queue


def bfs(adj_matrix, start_node):
    n = len(adj_matrix)
    visited = [False] * n
    queue = Queue()

    visited[start_node] = True
    queue.put(start_node)

    bfs_result = []

    while not queue.empty():
        current_node = queue.get()
        bfs_result.append(str(current_node))  # Store the node value as a string

        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.put(neighbor)

    return ' -> '.join(bfs_result)  # Join the node values with ' -> ' delimiter


