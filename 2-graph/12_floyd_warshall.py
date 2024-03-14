# Define infinity as a large enough value. This value will be used
# for vertices not connected to each other
INF = float('inf')

# Function to run Floyd-Warshall algorithm
def floyd_warshall(graph):
    # number of vertices in graph
    V = len(graph)
    
    # dist[][] will be the output matrix that will finally
    # have the shortest distances between every pair of vertices
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    
    # Add all vertices one by one to the set of intermediate vertices.
    # Before start of an iteration, we have shortest distances between all
    # pairs of vertices such that the shortest distances consider only the
    # vertices in the set {0, 1, 2, .. k-1} as intermediate vertices.
    # After the end of an iteration, vertex no. k is added to the set of
    # intermediate vertices and the set becomes {0, 1, 2, .. k}
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example graph represented as an adjacency matrix
# graph = [[0, 5, INF, 10],
#          [INF, 0, 3, INF],
#          [INF, INF, 0, 1],
#          [INF, INF, INF, 0]]

graph = [
    [0, 1, INF, INF, INF, 2],
    [1, 0, 2, INF, INF, INF],
    [INF, 2, 0, 1, 3, INF],
    [INF, INF, 1, 0, 1, INF],
    [INF, INF, 3, 1, 0, 1],
    [2, INF, INF, INF, 1, 0]
]

# Run the Floyd-Warshall algorithm
dist_matrix = floyd_warshall(graph)

# Print the shortest distance matrix
print("Shortest distances between every pair of vertices:")
for row in dist_matrix:
    print(" ".join(["{:<7}".format("INF" if i == INF else i) for i in row]))