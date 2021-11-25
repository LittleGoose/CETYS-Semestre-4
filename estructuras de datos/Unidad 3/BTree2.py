# Implementacion de un Arbol B
# Actividad de implementacion de un arbol B.


# JORGE AXEL CRUZ JIMENEZ 31973


# Clase nodo
class BNode:
    def __init__(self, m):
        self.keys = [None]*(m+1) #Llaves dentro de cada nodo
        self.children = [None]*(m+2) #Apuntadores de los hijos de los nodos
        self.isFull = False #bandera que indica si el nodo esta lleno
        self.n = 0 #contador de valores en el nodo
        self.m = m #es el grado maximo, el numero maximo de valores que puede tener cada nodo

    # Funcion para insertar valores en el nodo
    def insert(self, k):
        # En este caso el valor se inserta en el nodo, se ordenan de menor a mayor en la lista (nodo)
        # Despues de insertar se revisa si se tiene que hacer split o no
        # Si se hace split, se revisa despues si la raiz esta llena o no, y se hace otro split con otra funcion
        i = 0
        while i< self.n and self.keys[i]<k:
            i+=1
            print(i)

        if self.children[i] is None: #si es nodo hoja
            self._insert_nonFull(k, i)
        else:
            self.isFull = self.children[i].insert(k) #La bandera obtiene verdadero o falso dependiendo si al insertar
                                                    #el nodo esta lleno o tiene espacio para insertar
            if self.isFull == True: #si el nodo esta lleno, hace split del nodo
                self._split(i)
        if self.n > self.m: #si el nodo esta lleno, regresa True, de lo contrario False
            return True
        else:
            return False

    # Funcion para insertar el valor si hay un espacio disponible en el nodo
    # Inserta el valor al nodo si tiene espacio, y ordena los valores de menor a mayor dentro del nodo
    def _insert_nonFull(self, k, i):
        j = self.n
        while j > i:
            self.keys[j] = self.keys[j-1]
            self.children[j+1] = self.children[j]
            j-=1
        self.keys[i] = k
        self.children[i+1] = self.children[i]
        self.n+=1

    # Funcion para separar el nodo
    def _split(self, index):
        node = self.children[index] #Se hace una copia del nodo original
        left_child = BNode(node.m) #Se crean nodo izquierdo para guardar los valores menores al separar
        right_child = BNode(node.m) #Se crean nodo derecho para guardar los valores mayores al separar
        i = 0
        while i < node.m // 2:  #Se toma el roof de la mitad del grado del arbol
            #Se guardan los valores de las llaves en el nodo hijos izquierdo
            left_child.children[i] = node.children[i]
            left_child.keys[i] = node.keys[i]
            left_child.n+=1
            i+=1
        left_child.children[i] = node.children[i]
        mid = i #despues de terminar de guardar en nodo izquierdo, se guarda la posicion del punto medio
        # el punto medio es donde empezara a guardar en el nodo hijo derecho
        i+=1
        j=0
        while i < node.n:
            # Se guardan los valores de las llaves en el nodo hijo derecho
            right_child.children[j] = node.children[i]
            right_child.keys[j] = node.keys[i]
            right_child.n+=1
            j+=1
            i+=1
        right_child.children[j] = node.children[i]

        # ya que separa los nodos en hijos izquierdo y derecho, inserta el valor medio en la nueva raiz
        self._insert_nonFull(node.keys[mid], index)
        self.children[index] = left_child
        self.children[index+1] = right_child

    # Funcion que borra un elemento dentro del nodo
    def delete(self, node, index, father): #si el elemento esta en nodo hoja
        if self.children[index] is None:
            # node.keys[index] = None
            self.deleteLeafElement(node, index)
        else:
            self.deleteNotLeafElement(node, index)
        if len(node.keys) < node.m // 2:
            self.merge()
        else: return


    def deleteLeafElement(self, node, index):
        node.keys.pop(index)
        node.keys.append(None)
        self.n-=1

    def deleteNotLeafElement(self, node, index):
        if node.children[index]<node.children[index+1]:
            self.stealFromRight(node.children[index], index)
        else:
            self.stealFromLeft(node.children[index], index)

    def merge(self):
        pass

    def stealFromRight(self, node, i):
        pass

    def stealFromLeft(self, node, i):
        pass

#Clase Arbol B
class Btree:
    def __init__(self, m):
        self.root = BNode(m)
        self.m = m  #m es el grado maximo, es decir, el numero maximo de hijos que puede tener un nodo

    # Funcion para buscar un valor en el arbol, modo recursivo para recorrer el arbol
    def search(self, k, node=None, father=None):
        if node is not None:
            i = 0
            while i < node.n and k > node.keys[i]:
                i += 1
            if i < node.n and k==node.keys[i]:
                print("\nValue",k,"found at index", i, "in this node ->", node.keys, "Its father node value is:", father.keys[i])
                return (node, i, father[i])
            elif node.children[i] is None: #si el nodo es hoja
                print("Value Not Found")
                return None
            else:
                return self.search(k, node.children[i], node)
        else:
            return self.search(k, self.root, self.root)

    # Funcion principal para insertar
    def insert(self, k):
        node_full = self.root.insert(k) #el estado del nodo, si esta lleno sera True, de lo contrario False
        if node_full is True:
            # Si el nodo de la nueva raiz esta lleno, se hace split de la nueva raiz
            self._splitRoot(self.root)

    # Funcion principal para el borrado
    def delete(self, k):
        node, index, father = self.search(k)
        if node is None: return
        else: node.delete(node, index)

    # Funcion para separar la raiz del nodo
    # Similar al split del nodo
    def _splitRoot(self, node):
        left_child = BNode(node.m)
        right_child = BNode(node.m)
        index = 0
        while index < node.m // 2:
            left_child.children[index] = node.children[index]
            left_child.keys[index] = node.keys[index]
            left_child.n+=1
            index+=1
        left_child.children[index] = node.children[index]
        mid = index
        index+=1
        j = 0
        while index < node.n:
            right_child.children[j] = node.children[index]
            right_child.keys[j] = node.keys[index]
            right_child.n+=1
            j+=1
            index+=1
        right_child.children[j] = node.children[index]

        node.keys[0] = node.keys[mid]
        node.children[0] = left_child
        node.children[1] = right_child
        node.n=1

    # Funcion para mostrar el arbol
    def printTree(self):
        self._print(self.root)

    # Funcion auxiliar de impresion del arbol
    def _print(self, node, level=0):
        if node is not None:
            i = node.n-1
            while i >= 0:
                self._print(node.children[i+1], level+1)
                for j in range(level):
                    print("  ->  ", end="")
                print(node.keys[i])
                i-=1
            self._print(node.children[0], level+1)

def main():
    BT = Btree(4)
    BT.insert(111)
    BT.insert(96)
    BT.insert(84)
    BT.insert(16)
    BT.insert(25)
    BT.insert(44)
    BT.insert(130)
    BT.insert(420)
    BT.insert(15)
    BT.printTree()
    BT.delete(25)
    BT.printTree()
    print(BT.root.children[0].keys)
    BT.insert(50)
    BT.printTree()
    BT.delete(15)
    BT.delete(16)
    BT.printTree()
    print(BT.root.keys)
if __name__ == '__main__':
    main()

# JORGE AXEL CRUZ JIMENEZ 31973

# Ultima modificacion: 10/11/2021 10:10 PM PDT