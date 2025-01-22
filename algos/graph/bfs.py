def bfs(graph, start):
    """
    Perform Breadth-First Search on 'graph' starting from 'start'.
    'graph' is a dict {node: [neighbors]}.
    Returns the order in which nodes are visited.
    """
    visited = set()    # To track visited nodes
    order = []         # List to record the visitation order

    queue = [start]    # Initialize the queue with the start node
    head = 0           # Initialize the front pointer for the queue

    while head < len(queue):  # While there are elements in the queue
        current = queue[head]  # "Dequeue" an element from the front
        head += 1

        # Process current node if it hasn't been visited
        if current not in visited:
            visited.add(current)
            order.append(current)

            # Enqueue all unvisited neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order

# Example BFS usage:
if __name__ == "__main__":
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS order:", bfs(example_graph, 'A'))
