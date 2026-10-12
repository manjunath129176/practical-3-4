
import heapq

def prims(graph):
    n = len(graph)
    visited = [False] * n
    pq = [(0, 0)]
    total_cost = 0
    count = 0

    while pq:
        weight, vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True
        total_cost += weight
        count += 1

        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))

    if count != n:
        print("Minimum Spanning Tree does not exist")
    else:
        print("Minimum cost:", total_cost)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

prims(graph)
