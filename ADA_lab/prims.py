import sys

def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices  # Track vertices included in MST
    edge_count = 0
    selected[0] = True  # Start from vertex 0 (can be any)
    mst_edges = []
    total_cost = 0

    while edge_count < num_vertices - 1:
        minimum = sys.maxsize
        x = 0  # row index
        y = 0  # col index

        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if (not selected[j]) and graph[i][j]:  # edge exists and j not in MST
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        
        mst_edges.append((x, y, graph[x][y]))
        total_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    return mst_edges, total_cost

# Example graph as adjacency matrix (0 means no edge)
graph = [
    [0, 2, 3, 6],
    [2, 0, 0, 8],
    [3, 0, 0, 5],
    [6, 8, 5, 0]
]

mst, cost = prim_mst(graph)
print("Edges in MST (u, v, weight):")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")
print(f"Total cost of MST: {cost}")
