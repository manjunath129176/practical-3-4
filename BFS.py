from collections import deque

def BFS(adj):
    v = len(adj)
    visited = [False] * v
    res = []

    src = 0
    q = deque()

    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return res


adj = [
    [1, 5],
    [0, 2, 3, 4],
    [0, 3],
    [1],
    [6, 1],
    [1],
    [3]
]

print("BFS Traversal:", BFS(adj))
