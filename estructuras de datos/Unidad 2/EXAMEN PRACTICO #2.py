# CODIGO PARA EXAMEN PRACTICO #2
# EUMIR IRAM ABBUD OROZCO 33150

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

# CLASE ARBOL
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

# --- FUNCIONES FUERA DE LAS CLASES

# Funcion para ordenar los datos del arbol en "pre orden"           
def Pre_Order(curr_node):
    # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
    nodeList = []
    
    # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
    if curr_node is not None:
        # Consigue el nodo izquierdo
        nodeList = nodeList + Pre_Order(curr_node.getLeft())
        # Inserta el nodo actual a la lista
        nodeList.insert(0, curr_node.getLabel())
        # Consigue el nodo derecho
        nodeList = nodeList + Pre_Order(curr_node.getRight())
    # Regresa la lista completa
    return nodeList

# Funcion para imprimir visualmente el arbol binario 
def PrintBST(root, space) :
 
    # Si la raiz esta vacia la funcion se detiene
    if (root == None) :
        return
 
    # variable usada para incrementar el espacio entre los niveles de los nodos
    space += COUNT[0]
 
    # Se encuentra el hijo derecho
    PrintBST(root.right, space)
 
    # Se imprime el nodo actual despues del espacio utilizando la lista "COUNT"
    print()
    for i in range(COUNT[0], space):
        print(end = "-")
    print(root.label)
 
    # Se encuentra el hijo izquierdo
    PrintBST(root.left, space)

# Funcion para encontrar la altura del arbol binario
def height(root):
 
    # Si el arbol esta vacio regresa el valor de 0
    if root is None:
        return 0
    
    # Guarda la altura de cada nodo izquierdo y derecho
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    # Compara las 2 variables y regresa la que sea mayor sumandole 1 porque las listas en python empiezan en 0
    return max(leftAns, rightAns) + 1

#  --- CODIGO PARA CORRER EL PROGRAMA ---

'''INSTRUCCION 1'''
Recorrido_Manual = [67, 44, 22, 9, 37, 39, 50, 47, 85, 73, 90, 88, 94]
print(f"Recorrido manual de preorden: {Recorrido_Manual}")

'''INSTRUCCION 2'''
t = BinarySearchTree()
for num in Recorrido_Manual:
    t.insert(num)
COUNT =[10]
print(f"Recorrido por codigo de preorden: {Pre_Order(t.root)}")
PrintBST(t.root, 0)

'''INSTRUCCION 3'''
print(f'Altura del arbol: {height(t.root)}')

'''INSTRUCCION 4'''
print(f"Valor Max: {t.getMax().getLabel()}")
print(f"Valor Min: {t.getMin().getLabel()}")

'''INSTRUCCION 5'''
'''INSTRUCCION 6'''
'''INSTRUCCION 7'''
