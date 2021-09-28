class Nodo():
    def __init__(self, elemento):
        self.elemento = elemento
        self.psig = None
        self.pprev = None
        
    def GetElement(self):
        return self.elemento
    
class ListaSimple():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        No_nodos = 0

class ListaDoble():
    def setNodoalinicio(self, elemento):
        nuevo = Nodo(elemento)
        if self.getVacio() == True:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.psig = self.primero
            self.primero.pprev = nuevo
            self.primero = nuevo
        self.size += 1
        
    def setNodoalfinal(self, elemento):
        nuevo = Nodo(elemento)
        if self.getVacio() == True:
            self.primero = self.ultimo = nuevo
        else:
            aux = self.ultimo
            self.ultimo = aux.psig = nuevo
            self.ultimo.pprev = aux
        self.sieze += 1
            