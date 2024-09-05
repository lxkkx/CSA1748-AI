from collections import deque

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Function to find the position of the empty space
def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Function to generate new states by moving the empty space
def generate_new_states(state):
    new_states = []
    x, y = find_zero_position(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # Copy the current state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_states.append(new_state)
    
    return new_states

# BFS to find the solution
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(tuple(row) for row in current_state))
        
        if is_goal(current_state):
            return path
        
        for new_state in generate_new_states(current_state):
            state_tuple = tuple(tuple(row) for row in new_state)
            if state_tuple not in visited:
                queue.append((new_state, path + [new_state]))
                visited.add(state_tuple)

# Initial state of the puzzle
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Solve the puzzle
solution_path = bfs(initial_state)

# Print the solution path
for step, state in enumerate(solution_path):
    print(f"Step {step + 1}:")
    for row in state:
        print(row)
    print()
