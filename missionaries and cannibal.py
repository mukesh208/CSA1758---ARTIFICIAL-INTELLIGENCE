from collections import deque

def is_valid_state(state):
    m_left, c_left, m_right, c_right, _ = state  # Include the boat position in unpacking
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_neighbors(state):
    neighbors = []
    m_left, c_left, m_right, c_right, boat = state
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]  # Possible moves
    
    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')
        
        if is_valid_state(new_state):
            neighbors.append(new_state)
    
    return neighbors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal:
            return path + [current_state]
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    
    return None

def missionaries_and_cannibals():
    start = (3, 3, 0, 0, 'left')  # Initial state
    goal = (0, 0, 3, 3, 'right')  # Goal state
    
    solution = bfs(start, goal)
    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    missionaries_and_cannibals()
