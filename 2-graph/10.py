# Define the flow network graph using a dictionary
# The graph is represented as a dictionary with keys as node names
# Each node has a list of tuples representing outgoing edges (destination, capacity, flow)

flow_network = {
    's': [('a', 4, 2), ('b', 5, 4)],
    'a': [('c', 3, 2), ('e', 1, 0)],
    'b': [('d', 3, 3), ('e', 4, 1)],
    'c': [('t', 5, 2)],
    'd': [('t', 4, 4)],
    'e': [('c', 3, 0), ('d', 2, 1)],
    't': []  # The sink node has no outgoing edges
}

# Function to verify the law of conservation at a node in a flow network graph
def verify_conservation_at_node(node, graph):
    inflow = 0
    outflow = 0

    # Calculate total inflow to the node
    for n in graph:
        for edge in graph[n]:
            if edge[0] == node:
                inflow += edge[2]  # edge[2] is the flow

    # Calculate total outflow from the node
    for edge in graph[node]:
        outflow += edge[2]  # edge[2] is the flow

    # The law of conservation holds if inflow equals outflow
    return inflow == outflow

# Verify the law of conservation at nodes a, e, and d
conservation_a = verify_conservation_at_node('a', flow_network)
conservation_e = verify_conservation_at_node('e', flow_network)
conservation_d = verify_conservation_at_node('d', flow_network)

print(conservation_a, conservation_e, conservation_d)


def calculate_and_print_cut_capacity(S, T, graph):
    cut_capacity = 0
    print(f"Calculating the capacity of the cut between S = {S} and T = {T}:")

    # Check each node in S
    for node in S:
        # Consider all edges going from node to nodes in T
        for edge in graph[node]:
            if edge[0] in T:
                # edge[1] is the capacity
                cut_capacity += edge[1]
                print(f"Edge from {node} to {edge[0]} has capacity {edge[1]}.")

    print(f"Total capacity of the cut is: {cut_capacity}")
    return cut_capacity

S = ['s', 'a', 'b']
T = ['c', 'd', 'e', 't']

# Calculate and print the capacity of the (s,t)-cut
cut_capacity_process = calculate_and_print_cut_capacity(S, T, flow_network)


# Function to check if flow can be increased along a given path, print the process, and by how much
def check_increase_flow_path(path, graph):
    print(f"Checking if flow can be increased along the path {' -> '.join(path)}:")

    # Get the minimum residual capacity along the path
    # This will be the maximum amount by which we can increase the flow
    min_residual_capacity = float('inf')
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i+1]
        
        # Find the edge and compute the residual capacity
        for edge in graph[from_node]:
            if edge[0] == to_node:
                residual_capacity = edge[1] - edge[2]  # capacity - flow
                min_residual_capacity = min(min_residual_capacity, residual_capacity)
                print(f"Edge from {from_node} to {to_node} has flow {edge[2]} and capacity {edge[1]}, residual capacity is {residual_capacity}.")

    if min_residual_capacity > 0:
        print(f"The flow can be increased by {min_residual_capacity}.")
    else:
        print("The flow cannot be increased along this path.")

    return min_residual_capacity

# Define the path s -> b -> e -> d -> t
path = ['s', 'b', 'e', 'd', 't']

# Check if flow can be increased along the path and by how much
additional_flow = check_increase_flow_path(path, flow_network)

# Function to find all possible augmenting paths and their respective bottleneck (minimum residual capacity)
def find_augmenting_paths(graph):
    augmenting_paths = []
    nodes = list(graph.keys())
    
    def dfs(current_node, path, min_residual_capacity):
        # If we reach the sink node, store the path and its bottleneck capacity
        if current_node == 't':
            augmenting_paths.append((path, min_residual_capacity))
            return
        
        for edge in graph[current_node]:
            residual_capacity = edge[1] - edge[2]
            # If the edge has residual capacity and the destination node is not already in the path
            if residual_capacity > 0 and edge[0] not in path:
                # Continue depth-first search from the destination node
                dfs(edge[0], path + [edge[0]], min(min_residual_capacity, residual_capacity))
    
    # Start depth-first search from the source node
    for edge in graph['s']:
        residual_capacity = edge[1] - edge[2]
        if residual_capacity > 0:
            dfs(edge[0], ['s', edge[0]], residual_capacity)

    return augmenting_paths

# Find all possible augmenting paths from s to t
augmenting_paths = find_augmenting_paths(flow_network)

# Check if there are no augmenting paths, which would mean the flow is maximum
is_max_flow = len(augmenting_paths) == 0
print(augmenting_paths, is_max_flow)

