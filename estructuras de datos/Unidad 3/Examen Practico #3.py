# EXAMEN PRACTICO #3 PARCIAL #3
# Eumir Iram Abbud Orozco 33150

### CODIGO FUNCIONES ###
import networkx as nx                       # Importamos de libreria NetworkX para su uso en la impresion del grafo
import matplotlib.pyplot as plt             # Importamos de libreria de matplotlib para su uso en la impresion del grafo

class Vertice:                              # Clase para las vertices
    def __init__(self, n):                  # Inicializador de la clase, "n" == nombre del vertice
        self.nombre = n                     # Nombre del vertice se guarda con la variable "n" (redundate)
        self.vecinos = list()               # Se crea una lista abierta con los vecinos del vertice
        self.distancia = 9999               # Distancia entre vertices, "9999" == "infinito"
        self.color = 'white'                # Color del nodo (util para realizar los recorridos)
        self.p = None                       # Nodo anterior
        self.d = 0                          # Tiempo de descubrimiento
        self.f = 0                          # Tiempo de termino
        
    def AgregarVecino(self, v):             # Funcion para registrar los vecinos del vertice
        if v not in self.vecinos:           # Condicional que corre si "v" (el valor) no esta en la lista
            self.vecinos.append(v)          # Se agrega el valor de "v" en la lista.
            self.vecinos.sort()             # Reordena la lista (menor a mayor)

class Grafo:                                # Clase para el grafo
    def __init__(self):                     # Inicializador de la clase
        self.vertices = {}                  # Lista de vertices
        self.tiempo = 0

    def agregarVertice(self, vertice):                                              # Funcion para agregar vertices al grafo
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:    # Condicional que corre si la variable "vertice" ya fue usada con la clase "Vertice", y si
                                                                                    # esta vertice NO esta dentro de la lista "vertices"
            self.vertices[vertice.nombre] = vertice                                 # se agrega "vertice" a la lisat de "vertices" utilizando el nombre del vertice que se crea con la clase "Vertice"
            return True                                                             # Se termina la funcion, y regresa un "True"
        else:
            return False                                                            # Si condicional no se cumple, la funcion se termina y regresa un "False"

    def AgregarAristaDirigida(self, u, v):              # Funcion para agregar arista dirigida entre 2 vertices
        if u in self.vertices and v in self.vertices:   # Condicional que corre si “u” y “v” estan dentro de la lista de “vertices”
            for key, value in self.vertices.items():    # Ciclo que corre utilizando todos los valores de la lista “vertices”
                if key == u:                            # Condicional que corre si “key” == valor del vertice “u”
                    value.AgregarVecino(v)              # Se utiliza la funcion de “AgregarVecino” para agregar como vecino de “u” al vertice “v” / se indica que una artista apunta de vertice “u” a “v”
            return True                                 # La funcion termina y regresa el valor “True”
        else:
            return False                                # Si la condicional original no se cumple la funcion termina y regresa el valor de “False”

    # Funcion para el recorrido bfs
    def bfs(self, inicio):
        inicio.color = 'gray'
        inicio.distancia = 0
        inicio.p = None
        visitados = []
        Q = []
        Q.append(inicio)
        print("Recorrido BFS desde el nodo", inicio.nombre)
        print("\tVertice "+str(inicio.nombre+" con distancia de: "+str(inicio.distancia)))
        while Q:
            u = Q.pop(0)
            for v in u.vecinos:
                if self.vertices[v].color == 'white':
                    self.vertices[v].color = 'gray'
                    self.vertices[v].distancia = 0
                    self.vertices[v].distancia = u.distancia+1
                    self.vertices[v].p = u
                    Q.append(self.vertices[v])
                    visitados.append(self.vertices[v].nombre)
                    print("\tVertice "+str(self.vertices[v].nombre+" con distancia de: "+str(self.vertices[v].distancia)))
            u.color = 'black'

    # Funcion para el recorrido dfs
    def dfs(self, inicio):
        self.tiempo = 0
        for u in sorted(list(self.vertices.keys())):
            if self.vertices[u].color == 'white':
                self._dfs(self.vertices[u])

    # Funcion auxiliar para el recorrido dfs
    def _dfs(self, vertice):
        self.tiempo+=1
        vertice.d = self.tiempo
        vertice.color = 'gray'
        for v in vertice.vecinos:
            if self.vertices[v].color == 'white':
                self.vertices[v].p = vertice
                self._dfs(self.vertices[v])
        vertice.color = 'black'
        self.tiempo+=1
        vertice.f = self.tiempo

### CODIGO PARA CORRER EL PROGRAMA ###

grafo = nx.DiGraph()                # Se creo un grafo vacio, sin nodos y sin bordes, la funcion "DiGraph" hace que se muestre la dirección de las aristas.
                                    # "A" == Alejandra, "B" == Beatriz, "C" == Cesar, "D" == Dania, "E" == Ernesto
grafo.add_edges_from([('AB'),('AC'),('AD'),('BD'),('CB'),('CE'),('DA'),('DC'),('DE'),('EA'),('EB')])
nx.draw(grafo, with_labels=True)    # Dibujamos el grafo con los margenes
plt.show()                          # Mostramos el grafo visualmente
print('Los lideres del grupo serian Alejandra y Dania, ya que ellas son los nodos con mas peso')
# ULTIMA MODIFICAION: 11/25/2021 9:40 AM