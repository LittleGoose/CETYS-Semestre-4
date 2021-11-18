# Codigo para Teoria de Grafos
# Eumir Iram Abbud Orozco 33150

### CODIGO FUNCIONES ###
class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        
    def AgregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort
        
class GrafoNoDirigido:
    vertices = {}
    
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False
        
    def AgregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.AgregarVecino(v)
                if key == v:
                    value.AgregarVecino(u)
            return True
        else:
            return False
        
    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice "+key+" Sus vecinos son:"+str(self.vertices[key].vecinos))

class GrafoDirigido:
    vertices = {}
    
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False
        
    def AgregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.AgregarVecino(v)
            return True
        else:
            return False
        
    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice "+key+" Sus vecinos son:"+str(self.vertices[key].vecinos))

### CODIGO PARA CORRER EL PROGRAMA ###

### codigo de la maestra ###
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

# lista no dirigida  
g = GrafoNoDirigido()
a = Vertice('1')
g.agregarVertice(a)
for i in range (ord('1'), ord('6')):
    g.agregarVertice(Vertice(chr(i)))

edges = ['12', '15', "25", '23', '24', '34', '45', '43']

for edge in edges:
    g.AgregarArista(edge[:1], edge[1:])

print('Lista de Adyacencia (grafo no dirigido):')
for k,v in g.vertices.items():
    print("%s -> %s" %(k,v.vecinos))

# lista dirigida
f = GrafoDirigido()
b = Vertice('1')
f.agregarVertice(b)
for i in range (ord('1'), ord('7')):
    f.agregarVertice(Vertice(chr(i)))

aristas = ['12', '14', "25", '36', '35', '42', '54']

for arista in aristas:
    f.AgregarArista(arista[:1], arista[1:])
print('\nLista de Adyacencia (grafo dirigido):')
for k,v in f.vertices.items():
    print("%s -> %s" %(k,v.vecinos))
    
# ULTIMA MODIFICAION: 11/18/2021 9:46 AM