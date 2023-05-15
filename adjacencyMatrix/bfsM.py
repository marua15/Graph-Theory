from queue import Queue

def bfs(adj_matrix, start_node):
    n = len(adj_matrix)
    visited = [False] * n
    queue = Queue()

    visited[start_node] = True
    queue.put(start_node)

    while not queue.empty():
        current_node = queue.get()
        print(current_node)

        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.put(neighbor)
