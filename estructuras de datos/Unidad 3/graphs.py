# Grafos.


import networkx as nx  # Importamos de libreria NetworkX
import matplotlib.pyplot as plt  # Importamos de libreria


class Vertice():  # Clase que nos va a permitir ir creando nuestro vertices.
    def __init__(self, n):  # Método para inicializar valores.
        self.nombre = n
        self.vecinos = list()  # Lista de vecinos
        self.distancia = 9999 #distancia
        self.color = 'white' #color del nodo
        self.p = -1 #predecesor
        self.d = 0 #tiempo de descubrimiento
        self.t = 0 #tiempo de termino

    def agregarVecinos(self, v):  # Método para agregar los consiguientes.
        if v not in self.vecinos:  # Si v (el valor) no esta en la lista,
            self.vecinos.append(v)  # se agrega el valor de v en la lista.
            self.vecinos.sort()  # Modifica la lista.


class Grafo():
    vertices = {}  # Diccionario
    tiempo = 0

    def agregarVertice(self, vertice):  # Método para agregar los vertices.
        if isinstance(vertice,
                      Vertice) and vertice.nombre not in self.vertices:  # Método (isinstance) nos regresa verdadero o falso para verificar si el vertice es un objeto que ya tenemos
            # en Vertice, verifica si dentro de vertice.nombre existe o no, de no existir, entra e inserta.
            self.vertices[vertice.nombre] = vertice  # Inserta un nuevo vertice
            return True  # Regresa True
        else:  # De no ser asi,
            return False  # Regresa False

    def agregarArista(self, u, v):  # Método para agregar arista con grafos no dirigidos.
        if u in self.vertices and v in self.vertices:  # Si u esta en vertice y v esta en vertices, entonces:
            for key, value in self.vertices.items():  # Para llave con valor en los valores de vertices:
                if key == u:  # Si la llave es igual a u, entonces:
                    value.agregarVecinos(v)  # Agrega el valor en Vecinos en v.
                if key == v:  # Si la llave es igual a v, entonces:
                    value.agregarVecinos(u)  # Agrega el valor en Vecinos en u.
            return True  # Regresa verdadero
        else:  # De no ser así,
            return False  # regresa falso.

    def agregarArista2(self, u, v):  # Este método lo puse para poder realizar el grafo dirigido.
        if u in self.vertices and v in self.vertices:  # Si u esta en vertice y v esta en vertices, entonces:
            for key, value in self.vertices.items():  # Para llave con valor en los valores de vertices:
                if key == u:  # Si la llave es igual a u, entonces:
                    value.agregarVecinos(v)  # Agrega el valor en Vecinos en v.
            return True  # Regresa verdadero
        else:  # De no ser así,
            return False  # regresa falso.

    def ImprimirGrafo(self):
        for key in sorted(
                list(self.vertices.keys())):  # Hace la impresión desde llaves hasta que llegue al final de la lista.
            print("Vertice " + key + " sus vecinos son: " + str(self.vertices[key].vecinos))


g = Grafo()  # Auxiliar para llamar a la clase Grafo.

# Esto era un ejemplo:

# a = Vertice('A')
# for i in range(ord('A'),ord('K')):
#    g.agregarVertice(Vertice(chr(i)))
# edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ']

print("CASO 1, sin NetworkX: ")
# CASO 1, lista de Adyacencia (grafo no dirigido):
a = Vertice('1')  # Auxiliar para llamar la clase Vertice.
g.agregarVertice(a)
for i in range(ord('1'), ord('6')):
    g.agregarVertice(Vertice(chr(i)))
edges = ['12', '15', '25', '24', '23', '34', '54']  # Lista

for edge in edges:
    g.agregarArista(edge[:1], edge[1:])

for k, v in g.vertices.items():
    print("%s -> %s" % (k, v.vecinos))
g.ImprimirGrafo()

print(" ")
print("CASO 2, sin NetworkX: ")

# CASO 2, lista de adyacencia (grafo dirigido):
a = Vertice('1')
g.agregarVertice(a)
for i in range(ord('1'), ord('7')):
    g.agregarVertice(Vertice(chr(i)))
edges = ['12', '14', '25', '42', '35', '36', '54', '66']  # Lista

for edge in edges:
    g.agregarArista2(edge[:1], edge[1:])

for k, v in g.vertices.items():
    print("%s -> %s" % (k, v.vecinos))

g.ImprimirGrafo()

# Ejemplo del caso 1 de grafo no dirigido con NetworkX

X = nx.Graph()  # Se creo un grafo vacio, sin nodos y sin bordes. El nombre de la imagen es X.
X.add_edges_from([('12'), ('15'), ('25'), ('24'), ('23'), ('34'), ('54')])
nx.draw(X, with_labels=True)  # Margenes.
plt.show()
  # Lo mostramos.


# Ejemplo del caso 2, de grafo dirigido con NetworkX
#
# X = nx.DiGraph()                # Se creo un grafo vacio, sin nodos y sin bordes. El nombre de la imagen es X,
#                                 # el DiGraph, hace que se muestre la dirección a la que va.
# X.add_edges_from([('12'),('14'),('25'),('42'),('35'),('36'),('54'),('66')])
# nx.draw(X, with_labels=True) # Margenes.
# plt.show()                      # Lo mostramos.

