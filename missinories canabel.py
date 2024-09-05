from collections import deque

# Check if a state is valid
def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    if m_left >= 0 and m_right >= 0 and c_left >= 0 and c_right >= 0:  # No negative numbers
        if (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):  # Missionaries never outnumbered
            return True
    return False

# Check if a state is the goal state
def is_goal(state):
    m_left, c_left, boat, m_right, c_right = state
    return m_left == 0 and c_left == 0 and m_right == 3 and c_right == 3

# Get all possible next states from the current state
def get_successors(state):
    successors = []
    m_left, c_left, boat, m_right, c_right = state
    if boat == 'left':
        new_boat = 'right'
        potential_moves = [(-1, 0), (-2, 0), (0, -1), (0, -2), (-1, -1)]  # Possible moves: 1 or 2 missionaries, 1 or 2 cannibals, 1 of each
    else:
        new_boat = 'left'
        potential_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Reverse the moves

    for move in potential_moves:
        m, c = move
        new_state = (m_left + m, c_left + c, new_boat, m_right - m, c_right - c)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

# BFS algorithm to find the solution
def missionaries_and_cannibals():
    initial_state = (3, 3, 'left', 0, 0)
    frontier = deque([(initial_state, [])])  # Queue of (state, path)
    explored = set()

    while frontier:
        current_state, path = frontier.popleft()

        if current_state in explored:
            continue

        explored.add(current_state)

        if is_goal(current_state):
            return path + [current_state]

        for successor in get_successors(current_state):
            frontier.append((successor, path + [current_state]))

    return None  # No solution found

# Run the algorithm
solution = missionaries_and_cannibals()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
