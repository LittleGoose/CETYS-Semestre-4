# Programa para listas enlazadas

# Jorge Axel Cruz Jimenez 31973, Eumir Iram Abbud Orozco 33150

# Clase Nodo
class Node():

    # Constructor
    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    # Funcion para conseguir el siguiente nodo
    def get_next (self):
        return self.next_node

    # Funcion para designar el siguiente nodo
    def set_next (self, n):
        self.next_node = n

    # Funcion para obtener el contenido de un nodo
    def get_data (self):
        return self.data

    # Funcion para asignar el contenido a un nodo especifico
    def set_data (self, d):
        self.data = d

# Clase para lista ligada
class LinkedList ():

    # Constructor
    def __init__(self, r = None):
        # Nodo raiz
        self.root = r
        self.size = 0

    # Funcion para obtener el tamaño de la lista
    def get_size (self):
        return self.size

    # Funcion para añadir un nuevo nodo con su contenido a la lista
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
        
    # Funcion para remover un nodo junto con su contenido de la lista
    def remove (self, d):
        this_node = self.root
        prev_node = None

        # Funcion para encontrar la informacion que se desea eliminar
        while this_node:
            
            # Si se encuentra la informacion en el nodo actual, se elimina con sus instrucciones especificas
            # dependiendo si el nodo actual es el nodo raiz
            if this_node.get_data() == d:
                
                # Si el nodo actual no es el nodo raiz, vincula los nodos anterior y posterior 
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                
                # Si el nodo actual es el nodo raiz, asigna al nodo siguiente como nodo raiz
                else:
                    self.root = this_node.get_next()
                    self.size -= 1
                
                # Se encontro y elimino la informacion buscada 
                return True	
            
            # Si no se encuentra la informacion en el nodo actual, se pasa al siguiente nodo
            else:
                prev_node = this_node
                this_node = this_node.get_next()
                
        # No se encontro la informacion buscada
        return False

    # Funcion para saber si la informacion que buscamos existe en algun nodo de la lista
    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

# Codigo para correr el programa de prueba
lista = LinkedList()
lista.add(5)
lista.add(8)
lista.add(12)
print("size="+str(lista.get_size()))
lista.remove(8)
print("size="+str(lista.get_size()))
print(lista.remove(12))
print("size="+str(lista.get_size()))
print(lista.find(5))

# Ultima modificacion: 23/9/2021 8:45 PM PDT