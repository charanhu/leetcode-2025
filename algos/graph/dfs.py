from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search on 'graph' starting from 'start'.
    'graph' is a dict {node: [neighbors]}.
    Returns the order in which nodes are visited.
    """
    visited = set()          # Keep track of visited nodes
    order = []               # The order in which nodes are visited
    queue = deque([start])   # Initialize the queue with the start node

    while queue:
        current = queue.popleft()   # Dequeue the front node
        if current not in visited:
            visited.add(current)    # Mark as visited
            order.append(current)   # Record visitation
            
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
