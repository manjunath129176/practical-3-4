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


# User input
v = int(input("Enter number of vertices: "))

adj = []

for i in range(v):
    neighbours = list(map(int, input(
        f"Enter neighbours of vertex {i}: "
    ).split()))
    adj.append(neighbours)

print("BFS Traversal:", BFS(adj))
