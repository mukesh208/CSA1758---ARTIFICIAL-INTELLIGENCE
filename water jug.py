from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    queue = deque()
    visited = set()
    parent_map = {}
    initial_state = (0, 0)
    queue.append(initial_state)
    parent_map[initial_state] = None
    
    while queue:
        current_state = queue.popleft()
        x, y = current_state
        
        if x == target:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parent_map[current_state]
            path.reverse()
            
            print("Solution Found!")
            print(f"Steps to reach the target ({target} liters) in Jug 1:")
            for step, state in enumerate(path):
                print(f"Step {step}: Jug1 = {state[0]}, Jug2 = {state[1]}")
            return path
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        possible_states = [
            (jug1_capacity, y),
            (x, jug2_capacity),
            (0, y),
            (x, 0),
            (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),
            (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x)),
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
                parent_map[state] = current_state
    
    print("No solution exists.")
    return None


if __name__ == "__main__":
    print("Enter the capacities of the jugs and the target:")
    jug1_capacity = int(input("Capacity of Jug 1: "))
    jug2_capacity = int(input("Capacity of Jug 2: "))
    target = int(input("Target amount of water in Jug 1: "))
    
    if target > jug1_capacity:
        print("Target cannot be greater than the capacity of Jug 1.")
    else:
        solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
