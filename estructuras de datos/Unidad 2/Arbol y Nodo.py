class Node():
    def __init__(self):
        self.data = data
        self.left = None
        self.right = None
        self.root = None
        self.isright = False
        self.isleft = False
        
class Tree():
    def __init__(self):
        self.root = None
        
    def IsEmpty(self):
        if self.root == None:
            return True
        
    def Insert(self, data):
        NewNode = Node(data)
        if self.IsEmpty() == True:
            self.root = NewNode
        # investigar que poner en el else