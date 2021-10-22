# CODIGO PARA ARBOL BINARIO Y NODOS
# IRAM OROZCO 33150, y otros 2 que no me acuerdo quien son haha??

# Clase de nodo
class Node():
    
    # Inicializador
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.root = None
        self.isright = False
        self.isleft = False
    
    # Obtener el numero guardado en un nodo 
    def Get_Data(self):
        return self.data
    
    # Guardar un numero en un nodo
    def Set_Data(self, labdatael):
        self.data = data
    
    # Obtener el nodo que este a la derecha (apuntador izquierdo)
    def Get_Left(self):
        return self.left
    
    # Guardar un nodo a la derecha (apuntador izquierdo)
    def Set_Left(self, left):
        self.left = left
    
    # Obtener el nodo que este a la derecha (apuntador derecho)
    def Get_Right(self):
        return self.right
    
    # Guardar un nodo a la derecha (apuntador derecho)
    def Set_Right(self, right):
        self.right = right    
    
    # Obtener el nodo padre
    def Get_Parent(self):
        return self.root

    # Guardar un nodo como el nodo padre
    def Set_Parent(self, root):
        self.root = root
  
# Clase del arbol binario  
class BinaryTree():
    
    # Inicializador
    def __init__(self):
        self.root = None
    
    # funcion para checar si el arbol esta vacio
    def IsEmpty(self):
        if self.root == None:
            return True
    
    # Funcion para insertar un nodo al arbol
    def Insert(self, data):
        # Crea una variable para el nuevo nodo
        New_Node = Node(data)
        
        # Si el arbol esta vacio corre esta instruccion
        if self.IsEmpty():
            # Directamente guarda el nuevo nodo como el nodo raiz
            self.root = New_Node
        
        # Si el arbol NO esta vacio corre esta instruccion
        else:
            # Crea una variable y guarda en ella al nodo raiz
            curr_node = self.root
            
            # Condicional que corre mientras la variable "curr_node" tenga un dato guardado
            # Esta condicional termina cuando el apuntador usado para guardar el siguient dato apunta a un nodo no creado, y graba "None"
            while curr_node is not None:
                # Crea una variable y guarda el valor del nodo raiz en ella
                parent_node = curr_node
                
                # Si el valor que se quiere agregar al arbol es MENOR al valor del nodo guardado en "curr_node", corre esta instruccion
                if New_Node.Get_Data() < curr_node.Get_Data():
                    # Guarda en la variable el valor al que apunta el apuntador izquierdo del nodo actualmente guardado
                    curr_node = curr_node.Get_Left()
                
                # Si es MAYOR corre esta instruccion
                else:
                    # Guarda en la variable el valor al que apunta el apuntador derecho del nodo actualmente guardado
                    curr_node = curr_node.Get_Right()
            
            # Si el dato que queremos agregar es MENOR que el ultimo dato guardado en la variable "parent_node" corre esta instruccion
            # ("parent_node" deberia tener guardado un nodo hoja)
            if New_Node.Get_Data() < parent_node.Get_Data():
                # Guarda el dato como un nuevo nodo al lado izquierdo
                parent_node.Set_Left(New_Node)
            
            # Si es MAYOR corre esta instruccion
            else:
                # Guarda el dato como un nuevo nodo al lado derecho
                parent_node.Set_Right(New_Node)
            
            # Crea un apuntador que le indica al nodo creado que tiene un nodo padre
            New_Node.Set_Parent(parent_node)  
    
    # Funcion para ordenar los datos del arbol en "orden"
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
    def Pre_Order(self, curr_node):
        # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
        nodeList = []
        
        # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
        if curr_node is not None:
            nodeList = nodeList + Pre_Order(curr_node.Get_Left())
            nodeList.insert(0, curr_node.Get_Parent())
            nodeList = nodeList + Pre_Order(curr_node.Get_Right())
        return nodeList
    
    # Funcion para ordenar los datos del arbol en "post orden"
    def Post_Order(self, curr_node):
        # Crea una lista vacia donde guardar los datos del arbol en el orden deseado
        nodeList = []
        
        # Si el valor con el que se inicia NO es "None" (esta vacio), la funcion corre
        if curr_node is not None:
            nodeList = nodeList + Post_Order(curr_node.Get_Left())
            nodeList = nodeList + Post_Order(curr_node.Get_Right())
            nodeList.insert(0, curr_node.Get_Parent())
        return nodeList

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
                    

# CODIGO PARA QUE CORRA EL PROGRAMA
tree = BinaryTree()
list =[18,8,6,9,22,21,20,43]

for i in list:
    tree.Insert(i)

print(str(tree))

# ULTIMA MODIFICACION: IRAM ABBUD 11:48 PM 10/7/2021