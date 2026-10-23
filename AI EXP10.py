import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in best and best[node] <= g:
            continue
        best[node] = g

        for nxt, cost in graph[node]:
            ng = g + cost
            heapq.heappush(
                pq, (ng + h[nxt], ng, nxt, path + [nxt])
            )

print(astar('A', 'D'))
