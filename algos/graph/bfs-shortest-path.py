from collections import deque


def bfs_shortest_path(graph, start, target):
    # Queue for BFS
    queue = deque([start])
    # Set of visited nodes
    visited = {start}
    # Dictionary to keep track of each node's predecessor
    parent = {start: None}

    while queue:
        current = queue.popleft()

        # Stop when we reach the target
        if current == target:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Reconstruct the shortest path
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()  # Reverse the path to start from the source

    return path


# Example graph (unweighted)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C"],
    "H": ["E"],
}

# Find shortest path from 'A' to 'H'
shortest_path = bfs_shortest_path(graph, "A", "H")
print("Shortest Path:", shortest_path)
