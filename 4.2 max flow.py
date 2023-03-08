import collections


class Graph:
    """
    This class represents a directed graph using
    adjacency matrix representation.
    """

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        """
        Returns true if there is a path from
        source 's' to sink 't' in residual graph.
        Also fills parent[] to store the path.
        """

        # Mark all the vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def edmonds_karp(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def solution(entrances, exits, path):
    for i in range(len(path)):
        path[i] = [0] + path[i] + [0]

    super_entrance = [0] * (len(path) + 2)
    for entrance in entrances:
        super_entrance[entrance + 1] = float('inf')
    super_exit = [0] * (len(path) + 2)
    for exit in exits:
        path[exit][-1] = float('inf')
    path.insert(0, super_entrance)
    path.append(super_exit)
    g = Graph(path)
    return g.edmonds_karp(0, len(path) - 1)


# path = [
#     [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
#     [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
#     [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
#     [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
#     [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#     [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]
# print(solution([0, 1], [4, 5], path))

print(solution([0], [3], [[0, 7, 0, 0], [
      0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))

# g = Graph(path)

# source = 0; sink = 5

# print ("The maximum possible flow is %d " % g.edmonds_karp(source, sink))
