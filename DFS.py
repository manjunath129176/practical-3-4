def DFS(graph):
    V = len(graph)
    visited = [False] * V
    res = []

    src = 0
    visited[src] = True
    res.append(src)

    stack = [(src, iter(graph[src]))]

    while stack:
        curr, neighbour = stack[-1]

        try:
            i = next(neighbour)

            if not visited[i]:
                visited[i] = True
                res.append(i)
                stack.append((i, iter(graph[i])))

        except StopIteration:
            stack.pop()

    return res

V = int(input("Enter number of vertices: "))

graph = []

for i in range(V):
    neighbours = list(map(int, input(
        f"Enter neighbours of vertex {i}: "
    ).split()))
    graph.append(neighbours)

print("DFS Traversal:", DFS(graph))
