
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

# ========== BFS IMPLEMENTATION ==========
def bfs(graph, start, goal):
    visited = []
    queue = []
    
    visited.append(start)
    queue.append(start)
    
    print("BFS Traversal: ", end='')
    
    while queue:
        m = queue.pop(0)
        print(m, end=' ')
        
        if m == goal:
            print(f"\nBFS found goal: {goal}")
            return
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    print(f"\nBFS did not find goal: {goal}")

# ========== DFS IMPLEMENTATION (ITERATIVE) ==========
def dfs_iterative(graph, start, goal):
    visited = []
    stack = []
    
    stack.append(start)
    visited.append(start)
    
    print("DFS Iterative Traversal: ", end='')
    
    while stack:
        m = stack.pop()
        print(m, end=' ')
        
        if m == goal:
            print(f"\nDFS found goal: {goal}")
            return
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
    
    print(f"\nDFS did not find goal: {goal}")

# ========== DFS IMPLEMENTATION (RECURSIVE) ==========
visited_recursive = []

def dfs_recursive(graph, node, goal):
    if node not in visited_recursive:
        visited_recursive.append(node)
        print(node, end=' ')
        
        if node == goal:
            return True
        
        for neighbour in graph[node]:
            if dfs_recursive(graph, neighbour, goal):
                return True
        return False

# ========== MAIN PROGRAM ==========
print("=" * 60)
print("BFS vs DFS COMPARISON")
print("=" * 60)
print(f"\nGraph Adjacency List:")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")
print(f"\nStart Node: A")
print(f"Goal Node: I")
print()

print("=" * 60)
bfs(graph, 'A', 'I')
print()

print("=" * 60)
dfs_iterative(graph, 'A', 'I')
print()

print("=" * 60)
print("DFS Recursive Traversal: ", end='')
visited_recursive = []
result = dfs_recursive(graph, 'A', 'I')
print()
if result:
    print("DFS Recursive found goal: I")
else:
    print("DFS Recursive did not find goal: I")
print()

print("=" * 60)
print("COMPARISON SUMMARY")
print("=" * 60)
print(f"{'Parameter':<20} {'BFS':<20} {'DFS':<20}")
print("-" * 60)
print(f"{'Data Structure':<20} {'Queue (FIFO)':<20} {'Stack (LIFO)':<20}")
print(f"{'Traversal Order':<20} {'Level by level':<20} {'Depth first':<20}")
print(f"{'Finds Shortest Path?':<20} {'Yes':<20} {'No':<20}")
print(f"{'Memory Usage':<20} {'High (O(b^d))':<20} {'Low (O(bm))':<20}")
print(f"{'Complete?':<20} {'Yes':<20} {'No (may go infinite)':<20}")
print(f"{'Optimal?':<20} {'Yes':<20} {'No':<20}")

print("\n" + "=" * 60)
print("Program by: [Mahesh Sharma]")
print("Roll No: [19]")
