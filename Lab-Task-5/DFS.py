class Graph:
    def __init__(self, graph_dict=None):
        self.graph = graph_dict if graph_dict else {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[u].add(v)
        self.graph[v].add(u)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for node in self.graph[start] - visited:
            self.dfs(node, visited)
        return visited
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")
if __name__ == "__main__":
    graph_dict = {
        '0': {'1', '2'},
        '1': {'0', '3', '4'},
        '2': {'0'},
        '3': {'1'},
        '4': {'1', '2'}
    }
    g = Graph(graph_dict)
    print("DFS Traversal of Graph:")
    g.dfs('0')
    print("\n")
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    bt = BinaryTree(root)
    print("Preorder Traversal of Binary Tree:")
    bt.preorder(bt.root)
    print("\nInorder Traversal of Binary Tree:")
    bt.inorder(bt.root)
    print("\nPostorder Traversal of Binary Tree:")
    bt.postorder(bt.root)