
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

visited = []  # List for visited nodes
queue = []    # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("=" * 50)
print("BREADTH-FIRST SEARCH TRAVERSAL")
print("=" * 50)
print("BFS Order: ", end='')
bfs(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: [Your Name]")
print("Roll No: [Your Roll No]")