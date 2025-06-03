def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot == yroot:
        return False  # They are already in the same set

    # Union by rank
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    return True

def kruskal(vertices, edges):
    parent = {}
    rank = {}

    for v in vertices:
        parent[v] = v
        rank[v] = 0

    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  # Sort by weight

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Example input
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Cost Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total Cost:", cost)
