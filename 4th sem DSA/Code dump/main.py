class binarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key):
        # if tree is empty
        if self.data is None:
            self.data = key
        # if tree is not empty

        # Duplicate value
        if self.data == key:
            return None
        # If root key value is more than key
        if self.data > key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = binarySearchTree(key)
        # If root key value is less than ke y
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = binarySearchTree(key)


    def search(self, key):
        if self.data == key:
            return True
        if self.data < key:
            if self.right:
                self.right.search(key)
            return False
        else:
            if self.left:
                self.left.search(key)
            return False


    def preorder(self):
        if self.data:
            print(self.data, end = " ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


    def postorder(self):
        if self.data:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data,end = " ")


    def inorder(self):
        if self.data:
            if self.left:
                self.left.inorder()
            if self.data:
                print(self.data,end = " ")
            if self.right:
                self.right.inorder()
    
    
    def smallestNode(self):
        temp = self
        while temp.left:
            temp = temp.left
        return temp.data
        
    
    def largestNode(self):
        temp = self
        while temp.right:
            temp = temp.right
        return temp.data
        
        
root = binarySearchTree(80)
root.insert(8)
root.insert(123)
root.insert(56)
root.insert(2)
root.insert(7)

root.preorder()
print()
root.inorder()
print()
root.postorder()
print()
print(root.smallestNode())
print(root.largestNode())