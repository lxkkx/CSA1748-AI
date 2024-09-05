def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # Add the current node to the path and mark it as visited
    path.append(start)
    visited.add(start)

    # If the current node is the goal, return the path
    if start == goal:
        return path

    # Explore all adjacent nodes (neighbors)
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result:  # If a path is found, return it
                return result

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

path = dfs(graph, start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
