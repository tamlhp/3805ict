def bellman_ford(graph, source):
    # Initialize distance to all nodes to infinity, and source node to 0
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for edge in graph[node]:
                if distance[node] + edge[1] < distance[edge[0]]:
                    distance[edge[0]] = distance[node] + edge[1]

    # Check for negative weight cycles
    for node in graph:
        for edge in graph[node]:
            if distance[node] + edge[1] < distance[edge[0]]:
                print("Graph contains a negative weight cycle")
                return None

    return distance

# Design the graph
graph = {
    'A': [('B', 6), ('C', 5), ('D', 5)],
    'B': [('E', -1)],
    'C': [('B', -2), ('E', 1)],
    'D': [('C', -2), ('F', -1)],
    'E': [('F', 3)],
    'F': []
}

# Find shortest paths from the pink node (A)
source = 'A'
shortest_paths = bellman_ford(graph, source)

# Print the shortest paths from A
if shortest_paths:
    print("Shortest paths from node A:")
    for node, distance in shortest_paths.items():
        print(f"A to {node}: {distance}")
