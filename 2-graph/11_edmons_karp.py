from collections import deque

class Graph:
    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [row[:] for row in graph]  # make a copy for the residual graph
        self.ROW = len(graph)
        
    def bfs(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = deque()
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for ind, val in enumerate(self.residual_graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]
    
    def edmonds_karp(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        paths = []

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            path = []
            while(s != source):
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])
                path.insert(0, s)
                s = parent[s]
            path.insert(0, source)
            paths.append((path, path_flow))
            
            max_flow += path_flow
            
            v = sink
            while(v != source):
                u = parent[v]
                self.residual_graph[u][v] -= path_flow
                self.residual_graph[v][u] += path_flow
                v = parent[v]
                
        return max_flow, paths

# Making the graph a bit more complex
# graph = [[0, 16, 13, 0, 0, 0, 0],
#          [0, 0, 0, 12, 0, 0, 0],
#          [0, 4, 0, 0, 14, 0, 0],
#          [0, 0, 9, 0, 0, 0, 20],
#          [0, 0, 0, 7, 0, 4, 0],
#          [0, 0, 0, 0, 0, 0, 10],
#          [0, 0, 0, 0, 0, 0, 0]]

graph = [[0, 2, 10, 8, 0, 0, 0, 0],#s
         [0, 0, 0, 0, 6, 10, 0, 0],#a
         [0, 0, 0, 0, 6, 3, 2, 0],#b
         [0, 0, 5, 0, 0, 0, 3, 0],#c
         [0, 0, 0, 0, 0, 0, 0, 4],#d
         [0, 0, 0, 0, 0, 0, 0, 9],#e
         [0, 0, 0, 0, 0, 0, 0, 10],#f
         [0, 0, 0, 0, 0, 0, 0, 0],#t
         ]
g = Graph(graph)

source = 0  # Node 1
sink = 7    # Node 7
max_flow, paths = g.edmonds_karp(source, sink)
print("The maximum possible flow is:", max_flow)
print("The paths taken (path, flow) are:")
for path, flow in paths:
    print(f"{path} with flow = {flow}")
