# Lab: A* Search Algorithm
# Program by: [Your Name]
# Roll no: [Your Roll No]

# Step 1: Define the Graph (connections with edge costs)
graph = {
    'S': [('A', 5), ('B', 4)],
    'A': [('C', 3), ('D', 2)],
    'B': [('D', 2), ('E', 3)],
    'C': [('F', 2)],
    'D': [('F', 2), ('G', 1)],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Step 2: Define Heuristic Values (estimated distance to goal G)
heuristic = {
    'S': 10,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

# Step 3: A* Search Algorithm
def a_star(start, goal):
    # Queue stores (f_value, node, g_value, path)
    queue = [(heuristic[start], start, 0, [start])]
    g_cost = {start: 0}  # Best g(n) found so far
    visited = []          # List of visited nodes

    print("=" * 70)
    print("A* SEARCH ALGORITHM")
    print("=" * 70)
    print()
    print("Start Node:", start)
    print("Goal Node:", goal)
    print()
    print("Step | Current Node | g(n) | h(n) | f(n) | Path")
    print("-----|--------------|------|------|------|-----------------")

    step = 1

    while queue:
        # Sort by f value (smallest first)
        queue.sort()
        
        # Get node with smallest f
        f_val, current, g_val, path = queue.pop(0)

        # Skip if already visited
        if current in visited:
            continue

        print(f"{step:4} | {current:12} | {g_val:4} | {heuristic[current]:4} | {f_val:4} | {' -> '.join(path)}")
        step = step + 1

        # If goal found, return path
        if current == goal:
            print()
            print("=" * 70)
            print("GOAL FOUND!")
            print("=" * 70)
            print("Path:", ' -> '.join(path))
            print("Total Cost:", g_val)
            return path

        # Mark current as visited
        visited.append(current)

        # Explore neighbors
        for neighbor, edge_cost in graph[current]:
            if neighbor in visited:
                continue

            new_g = g_val + edge_cost

            # Check if better path found
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]
                new_path = path + [neighbor]
                queue.append((new_f, neighbor, new_g, new_path))

    print("Goal not found!")
    return None

# Step 4: Run the algorithm
a_star('S', 'G')