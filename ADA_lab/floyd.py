# Number of vertices in the graph
V = 4

# Floyd-Warshall Algorithm implementation
def floyd_warshall(graph):
    # Copy the input graph to distance matrix
    dist = [row[:] for row in graph]

    # Applying Floyd Warshall Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print_solution(dist)

# Function to print the solution
def print_solution(dist):
    print("Shortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

# Example graph represented as an adjacency matrix
# INF means there is no direct edge
INF = float('inf')
graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

# Call the function
floyd_warshall(graph)
