from collections import deque

def bfs(graph, start, goal):
    # Create a queue for BFS and enqueue the start node
    queue = deque([(start, [start])])  # Each element in the queue is a tuple (node, path_to_node)
    visited = set()  # Set to keep track of visited nodes

    while queue:
        current_node, path = queue.popleft()

        # If the current node is the goal, return the path
        if current_node == goal:
            return path

        # Mark the current node as visited
        visited.add(current_node)

        # Explore all adjacent nodes (neighbors)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # Return None if no path is found

# Example usage:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C']
}

start_node = 'A'
goal_node = 'G'

path = bfs(graph, start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
