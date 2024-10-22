from collections import deque

def water_jug_a_star(capacity, target):
    # Initial state: (0, 0) liters in both jugs
    start = (0, 0)
    goal = (target, 0)  # Goal state
    
    # Define possible actions
    def get_neighbors(state):
        x, y = state
        actions = [
            (capacity[0], y),  # Fill Jug 1
            (x, capacity[1]),  # Fill Jug 2
            (0, y),            # Empty Jug 1
            (x, 0),            # Empty Jug 2
            (min(x + y, capacity[0]), y - (min(x + y, capacity[0]) - x)),  # Pour Jug 2 to Jug 1
            (x - (min(x + y, capacity[1]) - y), min(x + y, capacity[1]))   # Pour Jug 1 to Jug 2
        ]
        return [(a, b) for a, b in actions if 0 <= a <= capacity[0] and 0 <= b <= capacity[1]]
    
    # Heuristic function: absolute difference from the target
    def heuristic(state):
        return abs(state[0] - target) + abs(state[1] - target)
    
    # Priority queue for A*
    open_set = []
    heapq.heappush(open_set, (heuristic(start), start))  # (f, state)
    
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor), neighbor))
    
    return []  # No solution found

# Water jug capacities and target
capacity = (4, 3)
target = 2

solution = water_jug_a_star(capacity, target)

# Print the solution path
for state in solution:
    print(f"Jug 1: {state[0]}, Jug 2: {state[1]}")
