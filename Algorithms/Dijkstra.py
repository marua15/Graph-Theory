import heapq
# module is a built-in module that provides an 
# implementation of the heap queue algorithm, also known as the priority queue algorithm.

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    # is a dictionary comprehension that initializes the distances dictionary 
    # with all nodes from the graph and sets their initial distances to infinity (float('inf')).
    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Pops (remove) the smallest item from the heap while maintaining the heap property.

        # Ignore outdated entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                # Pushes (add) an item onto the heap while maintaining the heap property.

    return distances