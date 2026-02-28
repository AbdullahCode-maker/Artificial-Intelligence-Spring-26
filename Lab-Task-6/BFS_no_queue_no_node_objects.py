class Graph:
    def __init__(self, graph_dict):
        self.graph = graph_dict
    def bfs_level(self, current_level_nodes, visited):
        next_level_nodes = []
        for node in current_level_nodes:
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                next_level_nodes.extend(self.graph.get(node, []))
        if next_level_nodes:
            self.bfs_level(next_level_nodes, visited)
    def bfs(self, start):
        print("BFS traversal without queue:")
        visited = set()
        self.bfs_level([start], visited)
graph_dict = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
    'G': [],
    'H': ['L'],
    'I': [],
    'K': ['M'],
    'L': [],
    'M': []
}
g = Graph(graph_dict)
g.bfs('A')