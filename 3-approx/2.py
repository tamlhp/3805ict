import numpy as np

"""
Problem Description: Given a list of cities and the distances between each pair of cities, 
the problem is to find the shortest possible route that visits each city exactly once and returns to the origin city.

Implementing a 2-approximation algorithm for the Traveling Salesman Problem (TSP) typically involves leveraging 
a minimum spanning tree (MST) of the graph representing the cities and distances. A well-known 2-approximation 
algorithm for TSP in metric spaces (where the triangle inequality holds) is based on constructing a MST, performing 
a preorder traversal of the MST to visit the vertices, and then returning to the start to complete the tour. 
This method is often referred to in relation to Christofides' algorithm, which offers a 1.5-approximation but is 
a bit more complex due to involving a matching step on odd-degree vertices.

Here's a simplified version of a 2-approximation algorithm for TSP using MST, demonstrated using Python:
- Construct a Minimum Spanning Tree (MST) for the graph.
- Perform a Preorder Traversal of the MST to get the order of visits.
- Create the TSP path by following the preorder traversal and return to the start.

Note: This approach assumes a complete graph (every pair of vertices is connected) and that the triangle 
inequality holds (the direct path between any two points is no longer than any indirect path).
"""


def prim_mst(cost):
    num_vertices = len(cost)
    in_mst = [False] * num_vertices
    parent = [-1] * num_vertices
    key = [float('inf')] * num_vertices
    key[0] = 0
    
    for _ in range(num_vertices):
        min_key = float('inf')
        for v in range(num_vertices):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        in_mst[u] = True
        
        for v in range(num_vertices):
            if cost[u][v] > 0 and not in_mst[v] and cost[u][v] < key[v]:
                key[v] = cost[u][v]
                parent[v] = u
    
    return parent

def preorder_traversal(parent, start):
    visit_order = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visit_order:
            visit_order.append(node)
            for child in reversed(range(len(parent))):
                if parent[child] == node:
                    stack.append(child)
    
    return visit_order

def tsp_2_approximation(cost):
    parent = prim_mst(cost)
    tour = preorder_traversal(parent, 0)
    tour.append(0)  # Return to start
    return tour

# Example usage
cost_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

tour = tsp_2_approximation(cost_matrix)
print("TSP tour (2-approximation):", tour)
