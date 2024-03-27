"""
The 2-approximation algorithm for the Vertex Cover problem is a simple, yet effective, greedy algorithm. 
The Vertex Cover problem is a classic example of a computational problem: given a graph, the goal is to 
find the minimum number of vertices such that every edge in the graph is incident to at least one vertex in this set. 
This problem is NP-hard, meaning that no polynomial-time algorithm is known to find the optimal solution for all instances.

A 2-approximation algorithm doesn't guarantee finding the minimum vertex cover but ensures that the number of 
vertices in the cover is at most twice the optimal number. This is what "2-approximation" signifies—it provides 
a solution within a factor of 2 of the optimal solution.
"""

"""
By including both u and v for each selected edge, the algorithm potentially doubles the count of vertices in the worst case, 
hence ensuring the size of the vertex cover found by the algorithm is at most twice the size of the optimal vertex cover.
"""
def two_approx_vertex_cover(graph):
    # Copy the graph to avoid modifying the input
    graph_copy = {u: set(v) for u, v in graph.items()}
    cover = set()

    while graph_copy:
        # Pick an arbitrary edge (u, v)
        u, neighbors = next(iter(graph_copy.items()))
        
        # Ensure there's at least one neighbor to pick; otherwise, continue to next vertex
        if not neighbors:
            graph_copy.pop(u, None)  # Remove vertex with no neighbors
            continue

        v = neighbors.pop()

        # Add both vertices to the vertex cover
        cover.add(u)
        cover.add(v)

        # Remove all edges incident to either u or v
        for vertex in [u, v]:
            for neighbor in list(graph.get(vertex, [])):  # Use graph here to avoid modifying while iterating
                graph_copy.get(neighbor, set()).discard(vertex)
            graph_copy.pop(vertex, None)  # Safely remove vertex without causing KeyError

    return cover

# Design a simple graph for demonstration
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': []  # An isolated vertex for demonstration
}

# Run the 2-approximation algorithm for vertex cover
vertex_cover = two_approx_vertex_cover(graph)

# Print the resulting vertex cover
print("Approximate Vertex Cover:", vertex_cover)
