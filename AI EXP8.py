graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for n in graph[node]:
        if n not in visited:
            dfs(n, visited)

dfs('A', set())
