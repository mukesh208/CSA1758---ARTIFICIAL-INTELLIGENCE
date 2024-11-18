import heapq

class PuzzleNode:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state  
        self.parent = parent
        self.move = move
        self.depth = depth  
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost  

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)  
    x, y = divmod(blank_idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = state[:]
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append(new_state)

    return neighbors


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  

def solve_8_puzzle(start, goal):
    open_set = []
    closed_set = set()

    start_node = PuzzleNode(start, None, None, 0, manhattan_distance(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            return reconstruct_path(current_node), current_node.depth

        closed_set.add(tuple(current_node.state))

        for neighbor in get_neighbors(current_node.state):
            if tuple(neighbor) in closed_set:
                continue

            g = current_node.depth + 1
            h = manhattan_distance(neighbor, goal)
            neighbor_node = PuzzleNode(neighbor, current_node, neighbor, g, g + h)

            heapq.heappush(open_set, neighbor_node)

    return None, -1  

start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution, steps = solve_8_puzzle(start_state, goal_state)
if solution:
    print("Solution found!")
    print(f"Number of steps required: {steps}")
    print("Moves:")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(state[i:i + 3])  
        print() 
else:
    print("No solution exists.")
