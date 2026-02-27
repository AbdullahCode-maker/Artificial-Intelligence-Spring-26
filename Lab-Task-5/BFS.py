import collections
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
    def bfs(self, root):
        visited = set()
        queue = collections.deque()
        visited.add(root)
        queue.append(root)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    print("Following is Breadth First Traversal:")
    g.bfs(0)