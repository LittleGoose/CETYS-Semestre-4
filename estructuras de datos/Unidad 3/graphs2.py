# Codigo para Teoria de Grafos
# Eumir Iram Abbud Orozco 33150, Jorge Axel Cruz Jimenes 31973

### CODIGO FUNCIONES ###
# import networkx as nx

class Vertice:  # Clase para las vertices
    def __init__(self, n):  # Inicializador de la clase, "n" == nombre del vertice
        self.nombre = n  # Nombre del vertice se guarda con la variable "n" (redundate)
        self.vecinos = list()  # Se crea una lista abierta con los vecinos del vertice
        self.distancia = 9999
        self.color = 'white'
        self.p = None #precedesor
        self.d = 0 #tiempo de descubrimiento
        self.f = 0 #tiempo de termino

    # Funcion para registrar los vecinos del vertice
    def AgregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()
# clase grafo
class Grafo:
    def __init__(self):
        vertices = {}
        tiempo = 0

    # Funcion para agregar vertices al grafo
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    # Funcion para agregar arista no dirigida entre 2 vertices
    def AgregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:  # Condicional que corre si “u” y “v” estan dentro de la lista de “vertices”
            for key, value in self.vertices.items():  # Ciclo que corre utilizando todos los valores de la lista “vertices”
                if key == u:  # Condicional que corre si “key” == al valor del vertice “u”
                    value.AgregarVecino(v)
                if key == v:
                    value.AgregarVecino(u)
        else:
            return False

    # Funcion para agregar arista dirigida entre 2 vertices
    def AgregarAristaDirigida(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.AgregarVecino(v)
            return True
        else:
            return False

    # Funcion para imprimir visualmente el grafo
    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice " + key + " Sus vecinos son:" + str(self.vertices[key].vecinos))

    # Funcion para imprimir el recorrido dfs
    def imprimeGrafoRecorrido(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice " + key)
            print("Descubierto/Termino: "+str(self.vertices[key].d)+"/"+str(self.vertices[key].f), "\n")

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

### Ejemplo ###
# g = Grafo()
# a = Vertice('A')
# g.agregarVertice(a)
# for i in range (ord('A'), ord('K')):
#     g.agregarVertice(Vertice(chr(i)))

# edges = ['AB', 'AE', 'BF', "CG", 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']

# for edge in edges:
#     g.AgregarArista(edge[:1], edge[1:])

# for k,v in g.vertices.items():
#     print("%s -> %s" %(k,v.vecinos))

def main():
    # grafo no dirigido
    g = Grafo()

    for i in range(ord('1'), ord('6')):
        g.agregarVertice(Vertice(chr(i)))

    edges = ['12', '15', "25", '23', '24', '34', '45', '43']

    for edge in edges:
        g.AgregarArista(edge[:1], edge[1:])

    print('Lista de Adyacencia (grafo no dirigido):')
    for k, v in g.vertices.items():
        print("%s -> %s" % (k, v.vecinos))

    print()
    g.bfs(g.vertices['1'])

    #grafo dirigido
    g2 = Grafo()
    for j in range(ord('1'), ord('7')):
        g2.agregarVertice(Vertice(chr(j)))

    edges2 = ['12', '14', "25", '36', '35', '42', '54', '66']

    for edge in edges2:
        g2.AgregarAristaDirigida(edge[:1], edge[1:])

    print('\nLista de Adyacencia (grafo dirigido):')
    for m, n in g2.vertices.items():
        print("%s -> %s" % (m, n.vecinos))

    print()
    g2.dfs(g2.vertices['1'])
    g2.imprimeGrafoRecorrido()

if __name__ == '__main__':
    main()

# ULTIMA MODIFICAION: 11/23/2021 6:35 PM