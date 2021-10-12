class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.root = None
        self.isright = False
        self.isleft = False
    
    def Get_Data(self):
        return self.data
    
    def Set_Data(self, labdatael):
        self.data = data
    
    def Get_Right(self):
        return self.right
    
    def Set_Right(self, right):
        self.right = right    
    
    def Get_Left(self):
        return self.left
    
    def Set_Left(self, left):
        self.left = left
        
    def Get_Root(self):
        return self.root

    def Set_Root(self, root):
        self.root = root
    
class BinaryTree():
    def __init__(self):
        self.root = None
        
    def IsEmpty(self):
        if self.root == None:
            return True
        
    def Insert(self, data):
        New_Node = Node(data)
        if self.IsEmpty():
            self.root = New_Node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if New_Node.Get_Data() < curr_node.Get_Data():
                    curr_node = curr_node.Get_Left()
                else:
                    curr_node = curr_node.Get_Right()
            if New_Node.Get_Data() < parent_node.Get_Data():
                parent_node.Set_Left(New_Node)
            else:
                parent_node.Set_Right(New_Node)
            New_Node.Set_Root(parent_node)  
                
    def Pre_Order(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + Pre_Order(curr_node.Get_Left())
            nodeList.insert(0, curr_node.Get_Root())
            nodeList = nodeList + Pre_Order(curr_node.Get_Right())
        return nodeList
            
    def In_Order(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.Insert(0, curr_node)
            nodeList = nodeList + self.In_Order(curr_node.Get_Left())
            nodeList = nodeList + self.In_Order(curr_node.Get_Right())
        return nodeList

    def Post_Order(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + Post_Order(curr_node._Left())
            nodeList = nodeList + Post_Order(curr_node.Get_Right())
            nodeList.insert(0, curr_node.Get_Root())
        return nodeList

# CODIGO PARA QUE CORRA EL PROGRAMA
tree = BinaryTree()
list =[18,8,6,9,22,21,20,43]

for i in range(len(list)):
    tree.Insert(list[i])

print(tree.Pre_Order(list))

# ULTIMA MODIFICACION: IRAM ABBUD 11:48 PM 10/7/2021