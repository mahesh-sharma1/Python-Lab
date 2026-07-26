# Lab: Depth-First Search (DFS) - Iterative
# Program by: [Your Name]
# Roll no: [Your Roll No]

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
stack = []    # Initialize a stack

def dfs_iterative(visited, graph, node):
    stack.append(node)
    visited.append(node)

    while stack:
        m = stack.pop()
        print(m, end=' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

print("=" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (ITERATIVE)")
print("=" * 50)
print("DFS Order: ", end='')
dfs_iterative(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: [Your Name]")
print("Roll No: [Your Roll No]")