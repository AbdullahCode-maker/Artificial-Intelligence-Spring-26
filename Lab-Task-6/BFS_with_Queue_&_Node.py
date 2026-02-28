from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
class Graph:
    def __init__(self):
        self.nodes = {}
    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].neighbors.append(self.nodes[v])
    def bfs(self, start):
        print("BFS traversal with queue:")
        visited = set()
        queue = deque()
        visited.add(start)
        queue.append(self.nodes[start])
        while queue:
            current = queue.popleft()
            print(current.data, end=" ")
            for neighbor in current.neighbors:
                if neighbor.data not in visited:
                    visited.add(neighbor.data)
                    queue.append(neighbor)
g = Graph()
edges = [
    ('A','B'), ('A','C'),
    ('B','D'), ('B','E'),
    ('C','F'),
    ('D','G'), ('D','H'),
    ('F','I'), ('F','K'),
    ('H','L'),
    ('K','M')
]
for u, v in edges:
    g.add_edge(u, v)
g.bfs('A')