class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
        else:
            print("Value already exists in tree.")
            
    def delete(self, data):
        if self.root is None:
            print("Tree is empty.")
        else:
            self.root = self._delete(data, self.root)
            
    def _delete(self, data, node):
        if node is None:
            print("Value not found in tree.")
        elif data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                temp = self._find_max(node.left)
                node.data = temp.data
                node.left = self._delete(temp.data, node.left)
        return node
        
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node
        
    def inorder_traversal(self):
        if self.root is None:
            print("Tree is empty.")
        else:
            self._inorder_traversal(self.root)
            
    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.data)
            self._inorder_traversal(node.right)
