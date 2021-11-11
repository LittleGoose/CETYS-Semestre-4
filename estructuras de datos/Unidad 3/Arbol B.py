# Codigo para Arboles B
# Stephanie Gonzalez 33892, David Roldan 27292, Iram Abbud 33150

class Nodo:                             # Creacion de clase NODO
    
    def __init__(self, t):              # Inicializador de la clase
        self.hijos = list()             # los apuntadores a los nodos hijos (numeros entre numeros ej. 9 entre 7 y 11)
        self.llaves = list()            # los datos que estan dentro del nodo / las "claves" 
        self.hoja = 1                   # 
        self.n = 0                      # numero de llaves?
        
        for k in range(2*t):            # numero max de datos que pueden estar dentro de un nodo / num max de "claves" dentro de una "pagina"
            self.llaves.append([None])
        for k in range(2*t+1):          # numero de max de hijos que puede tener cada nodo
            self.hijos.append([None])
            
class ArbolB:                           # creacion de la clase ARBOL B
    
    def __init__(self, grado_min):
        self.raiz = None
        self.t = grado_min
        
    def bTreeCreate(self):
        if self.raiz == None:
            self.raiz = Nodo(self.t)
        return self.raiz

    def bTreeSplitChild(self,x,i):
        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t-1
        
        for j in range(1, self.t):
            z.llaves[j] = y.llaves[j+self.t]
            y.llaves[j+self.t] = None
        
        if y.hoja == 0:
            for j in range(1,self.t+1):
                z.hijos[j] = y.hijos[j+self.t]
                y.hijos[j+self.t] = None
        y.n = self.t-1
        
        for j in range (x.n+1, i, -1):
            x.hijos[j+1] = x.hijos[j]
        x.hijos[i+1] = z
        
        for j in range(x.n,i-1,-1):
            x.llaves[j+1] = x.llaves[j]
        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n+1
        
    def bTreeInsertNonFull(self,x,k):
        i = x.n
        if x.hoja == 1:
            while i>=1 and k<x.llaves[i]:
                x.llaves[i+1] = x.llaves[i]
                i = i-1
            x.llaves[i+1] = k
            x.n = x.n+1
        else:
            while i>=1 and k<x.llaves[i]:
                i=i-1
            i = i+1
            if x.hijos[i].n == 2*self.t-1:
                self.bTreeSplitChild(x,i)
                if k > x.llaves[i]:
                    i = i+1
        self.bTreeInsertNonFull(x.hijos[i], k)
   
    def bTreeInsert(self, nodo, k):
        r = self.raiz
        if r.n == 2*self.t-1:
            s = Nodo(self.t)
            self.raiz=s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            self.bTreeSplitChild(s,1)
            self.bTreeInsertNonFull(s,k)
        else:
            self.bTreeInsertNonFull(r,k)
            
BT = ArbolB(2)
actual = BT.bTreeCreate()
print("Nodo Creado.")
print(BT.raiz.llaves)
BT.bTreeInsert(actual,111)
BT.bTreeInsert(actual,96)
BT.bTreeInsert(actual,84)
BT.bTreeInsert(actual,16)
# FECHA DE ULTIMA EDICION: 11/9/2021 9:28 AM