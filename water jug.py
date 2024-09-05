from collections import deque

def is_goal_state(state, d):
    return state[0] == d or state[1] == d

def get_possible_states(state, m, n):
    x, y = state
    return [
        (m, y),  # Fill Jug 1
        (x, n),  # Fill Jug 2
        (0, y),  # Empty Jug 1
        (x, 0),  # Empty Jug 2
        (x - min(x, n - y), y + min(x, n - y)),  # Pour Jug 1 into Jug 2
        (x + min(y, m - x), y - min(y, m - x))   # Pour Jug 2 into Jug 1
    ]

def bfs_water_jug(m, n, d):
    visited = set()
    queue = deque([((0, 0), [])])  # Start with both jugs empty

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal_state(current_state, d):
            return path + [current_state]

        for new_state in get_possible_states(current_state, m, n):
            if new_state not in visited:
                queue.append((new_state, path + [current_state]))

    return None  # No solution found

def print_solution(solution):
    if solution:
        print("Solution path:")
        for step in solution:
            print(f"Jug 1: {step[0]} liters, Jug 2: {step[1]} liters")
    else:
        print("No solution found")

# Example usage:
m = 4  # Capacity of Jug 1
n = 3  # Capacity of Jug 2
d = 2  # Desired amount of water

solution = bfs_water_jug(m, n, d)
print_solution(solution)
