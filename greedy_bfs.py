# Lab: Greedy Best-First Search
# Program by: [Your Name]
# Roll no: [Your Roll No]

# Step 1: Define the Graph (connections between nodes)
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
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

# Step 3: Greedy BFS Algorithm
def greedy_bfs(start, goal):
    # Queue stores (h_value, node, path)
    queue = [(heuristic[start], start, [start])]
    visited = []  # Keep track of visited nodes

    print("=" * 60)
    print("GREEDY BEST-FIRST SEARCH")
    print("=" * 60)
    print()
    print("Step | Current Node | h(n) | Path")
    print("-----|--------------|------|-----------------")

    step = 1

    while queue:
        # Sort by heuristic value (smallest first)
        queue.sort()
        
        # Get the node with smallest h(n)
        h_val, current, path = queue.pop(0)

        # Skip if already visited
        if current in visited:
            continue

        print(f"{step:4} | {current:12} | {h_val:4} | {' -> '.join(path)}")
        step = step + 1

        # If goal found, return path
        if current == goal:
            print()
            print("=" * 60)
            print("GOAL FOUND!")
            print("=" * 60)
            print("Path:", ' -> '.join(path))
            return path

        # Mark current as visited
        visited.append(current)

        # Add all unvisited neighbors to queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((heuristic[neighbor], neighbor, new_path))

    print("Goal not found!")
    return None

# Step 4: Run the algorithm
greedy_bfs('S', 'G')