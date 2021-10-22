# Declaramos la clase "Node"
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

        # Métodos para asignar nodos
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)      
    
    # Operación de borrado
    def delete(self, label):
        
        # Si el arbol NO esta vacio, continua el codigo
        if (not self.empty()):
            
            # llama la funcion de buscar el nodo con el  numero que estamos buscando 
            # y si lo encuentra lo asigna a la variable "node"
            node = self.getNode(label)
            
            # Si el valor encontrado SI esta en el arbol, el codigo sigue
            if(node is not None):
                
                # Si el nodo que queremos borrar NO tiene apuntadores, corre esto (0 hijos, nodo hoja)
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                    
                # Si SOLAMENTE el apuntador de la derecha del nodo que queremos borrar existe, corre esto (1 hijo, derecho)
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                    
                # Si SOLAMENTE el apuntador de la izquierda del nodo que queremos borrar existe, corre esto (1 hijo, izquierdo)
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                    
                # Si el nodo que queremos borrar tiene 2 apuntadores, corre esto  (2 hijos)
                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    node.setLabel(tmpNode.getLabel())
    
    # funcion para buscar un nodo con un valor dado
    def getNode(self, label):
        
        # Crea una variable para el nodo
        curr_node = None
        

        if(not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    # Funcion para reasignar Nodos
    def __reassignNodes(self, node, newChildren):
        
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
            
        if(node.getParent() is not None):
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    # def __str__(self):
    #     list = self.__InOrderTraversal(self.root)
    #     str = ""
    #     for x in list:
    #         str = str + " " + x.getLabel().__str__()
    #     return str

def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList

def In_Order(self, curr_node):
        # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
        nodeList = []
        
        # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
        if curr_node is not None:
            nodeList.Insert(0, curr_node)
            nodeList = nodeList + self.In_Order(curr_node.Get_Left())
            nodeList = nodeList + self.In_Order(curr_node.Get_Right())
        return nodeList

    # Funcion para ordenar los datos del arbol en "pre orden"           
def Pre_Order(curr_node):
    # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
    nodeList = []
    
    # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
    if curr_node is not None:
        nodeList = nodeList + Pre_Order(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + Pre_Order(curr_node.getRight())
    return nodeList

# Funcion para ordenar los datos del arbol en "post orden"
def Post_Order(curr_node):
    # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
    nodeList = []
    
    # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
    if curr_node is not None:
        nodeList = nodeList + Post_Order(curr_node.getRight())
        nodeList = nodeList + Post_Order(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
    return nodeList


'''
Ejemplo
                8
                / 
            3   10
            /     
            1   6    14
                /    /
            4   7 13 
'''

'''
Ejemplo luego del borrado
                7
                / 
            1   4

'''
# Instancia del árbol binario de búsqueda
t = BinarySearchTree()
#Insertamos los elementos
t.insert(8)
t.insert(3)
t.insert(6)
t.insert(1)
t.insert(10)
t.insert(14)
t.insert(13)
t.insert(4)
t.insert(7)

print(str(t))

if(t.getNode(6) is not None):
    print("El elemento 6 existe")
else:
    print("El elemento 6 no existe")

if(t.getNode(-1) is not None):
    print("El elemento -1 existe")
else:
    print("El elemento -1 no existe")

if(not t.empty()):
    print("Valor Max: " + str(t.getMax().getLabel()))
    print("Valor Min: " + str(t.getMin().getLabel()))

# t.delete(13)
# t.delete(10)
# t.delete(8)
# t.delete(3)
# t.delete(6)
# t.delete(14)

# Obtenemos todos los elementos del árbol en preorden
# list = t.traversalTree(InPreOrder, t.root)
# for x in list:
#     print(list)

print(str(InPreOrder(t.root)))
print(str(Pre_Order(t.root)))
print(str(Post_Order(t.root)))
