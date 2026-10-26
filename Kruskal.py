
def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])

    graph = [[v] for v in vertices]
    mst = []
    cost = 0

    for i, j, weight in edges:
        grp_i = None
        grp_j = None

        for g in graph:
            if i in g:
                grp_i = g
            if j in g:
                grp_j = g

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight
            grp_i.extend(grp_j)
            graph.remove(grp_j)

    return mst, cost


n = int(input("Enter number of vertices: "))
vertices = list(range(n))

m = int(input("Enter number of edges: "))
edges = []

print("Enter each edge as: source destination weight")

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst, cost = kruskal(vertices, edges)

print("\nMinimum Spanning Tree:")
for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Total cost:", cost)
