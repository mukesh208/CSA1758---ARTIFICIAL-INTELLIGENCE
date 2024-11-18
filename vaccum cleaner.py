from collections import deque

def is_goal_state(state, grid_size):
    return all(state[x][y] == 0 for x in range(grid_size[0]) for y in range(grid_size[1]))

def get_neighbors(state, position, grid_size):
    neighbors = []
    x, y = position
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size[0] and 0 <= ny < grid_size[1]:
            new_state = [row[:] for row in state]
            neighbors.append(((nx, ny), new_state))
    
    if state[x][y] == 1:
        new_state = [row[:] for row in state]
        new_state[x][y] = 0
        neighbors.append(((x, y), new_state))
    
    return neighbors

def bfs(initial_state, initial_position, grid_size):
    queue = deque([(initial_position, initial_state, [])])
    visited = set()
    visited.add((initial_position, tuple(map(tuple, initial_state))))
    
    while queue:
        position, state, path = queue.popleft()
        
        if is_goal_state(state, grid_size):
            return path + [position]
        
        for neighbor_position, neighbor_state in get_neighbors(state, position, grid_size):
            neighbor_repr = (neighbor_position, tuple(map(tuple, neighbor_state)))
            if neighbor_repr not in visited:
                visited.add(neighbor_repr)
                queue.append((neighbor_position, neighbor_state, path + [position]))
    
    return None

def vacuum_cleaner():
    grid_size = tuple(map(int, input("Enter grid size (rows columns): ").split()))
    grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
    dirty_positions = int(input("Enter the number of dirty cells: "))
    
    for _ in range(dirty_positions):
        x, y = map(int, input("Enter dirty cell position (row column): ").split())
        grid[x][y] = 1

    initial_position = tuple(map(int, input("Enter vacuum cleaner's initial position (row column): ").split()))

    solution_path = bfs(grid, initial_position, grid_size)
    if solution_path:
        print("Solution found!")
        print("Path taken by the vacuum cleaner:")
        for step, pos in enumerate(solution_path):
            print(f"Step {step}: {pos}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    vacuum_cleaner()
