from collections import deque

# Graph representation using adjacency list
cities = {
    'Islamabad': ['Rawalpindi', 'Lahore', 'Peshawar'],
    'Rawalpindi': ['Islamabad', 'Peshawar', 'Quetta'],
    'Peshawar': ['Islamabad', 'Rawalpindi', 'Quetta'],
    'Lahore': ['Islamabad', 'Multan', 'Quetta'],
    'Multan': ['Lahore', 'Karachi', 'Quetta'],
    'Quetta': ['Rawalpindi', 'Peshawar', 'Multan', 'Karachi'],
    'Karachi': ['Multan', 'Quetta']
}


# Function to perform BFS and find the shortest path
def bfs_shortest_path(graph, start, goal):
    # Create a queue for BFS and a dictionary to store paths
    queue = deque([[start]])
    visited = set()

    # Perform BFS
    while queue:
        path = queue.popleft()
        city = path[-1]

        # If the goal is reached, return the path
        if city == goal:
            return path

        # If the city is not visited, mark it as visited
        if city not in visited:
            visited.add(city)

            # Get neighbors of the current city
            for neighbor in graph[city]:
                new_path = list(path)  # Make a new copy of the current path
                new_path.append(neighbor)  # Append the neighbor to the path
                queue.append(new_path)

    # If no path is found, return None
    return None


# Function to print the shortest path
def print_shortest_path(graph, start, goal):
    path = bfs_shortest_path(graph, start, goal)
    if path:
        print(f"The shortest path from {start} to {goal} is: {' -> '.join(path)}")
    else:
        print(f"No path found between {start} and {goal}.")


# Find the shortest path from Islamabad to Karachi
print_shortest_path(cities, 'Islamabad', 'Karachi')
