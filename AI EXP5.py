from collections import deque

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

q = deque([((3, 3, 1), [])])
visited = set()

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state in visited:
        continue
    visited.add(state)
    path = path + [state]

    if state == (0, 0, 0):
        for step in path:
            print(step)
        break

    for dm, dc in moves:
        if boat == 1:
            nxt = (m-dm, c-dc, 0)
        else:
            nxt = (m+dm, c+dc, 1)

        if valid(nxt[0], nxt[1]):
            q.append((nxt, path))
