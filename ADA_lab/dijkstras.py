import heapq

def dijkstra(graph, start):
    # Priority queue to hold vertices to explore
    priority_queue = [(0, start)]
    # Dictionary to hold shortest distance to each vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # Dictionary to store the path
    previous = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if we already found a better path
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Relaxation step
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


# Example graph as an adjacency list
# Each key is a node and value is a list of tuples (neighbor, weight)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)],
}

start_node = 'D'
distances, previous = dijkstra(graph, start_node)

print("Shortest distances from", start_node)
for node in distances:
    print(f"{start_node} -> {node}: {distances[node]}")
