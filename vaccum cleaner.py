# Simple Vacuum Cleaner Agent

def vacuum_cleaner(grid):
    # Track the position of the vacuum cleaner
    pos = [0, 0]
    
    # Traverse the grid
    for i in range(2):
        for j in range(2):
            pos = [i, j]
            if grid[i][j] == 1:
                print(f"Cleaning dirt at position {pos}")
                grid[i][j] = 0
            else:
                print(f"Position {pos} is already clean")
    
    print("All positions are clean!")
    return grid

# Example grid (1 = dirty, 0 = clean)
grid = [
    [1, 0],
    [0, 1]
]

# Run the vacuum cleaner
cleaned_grid = vacuum_cleaner(grid)

# Output the final grid state
print("Final grid state:")
for row in cleaned_grid:
    print(row)
