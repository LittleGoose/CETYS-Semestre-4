# Codigo para Arboles B
# Stephanie Gonzalez 33892, David Roldan 27292, Iram Abbud 33150

class Nodo:                             # Creacion de clase NODO
    
    def __init__(self, t):              # Inicializador de la clase, t == 
        self.hijos = list()             # los apuntadores a los nodos hijos (numeros entre numeros ej. 9 entre 7 y 11)
        self.llaves = list()            # los datos que estan dentro del nodo / las "claves" 
        self.hoja = 1                   # num de hoja == num de nodo en la lista de nodos, 
                                        # 1 == principio y el final CUANDO ESTA SOLO, 0 == nodo padre, # == # de nodo en la lista de nodos (redundante)
        self.n = 0                      # numero de llaves que existen dentro del nodo / num de datos actuales dentro de 1 nodo
        
        for k in range(2*t):            # numero max de datos que pueden estar dentro de un nodo / num max de "claves" dentro de una "pagina"
            self.llaves.append([None])
        for k in range(2*t+1):          # numero de max de hijos que puede tener cada nodo
            self.hijos.append([None])
            
class ArbolB:                           # creacion de la clase ARBOL B
    
    def __init__(self, grado_min):      # inicializador de la clase, grado_min == cantidad minima de datos dentro de un 
                                        # nodo / num min de "claves" dentro de una "pagina" EXCEPTO en la raiz
        self.t = grado_min              # t == numero min de datos dentro de un nodo que no sea la raiz (explicacion redundate)
        self.raiz = None                # raiz empieza siendo None porque no existe arbol, y ese arbol se crea con la funcion "bTreeCreate"
        
    def bTreeCreate(self):              # funcion para crear la raiz del arbol, o nodo 0 / "pagina" 0
        if self.raiz == None:           # operacion CONDICIONAL que solo corre si no existe raiz del arbol
            self.raiz = Nodo(self.t)    # raiz es todo el NODO completo, la pagina creada y lista para llenar con datos
        return self.raiz                # creacion del nodo raiz / nodo 0 / primer pagina / pagina 0

    def bTreeInsert(self, nodo, k):     # funcion para insertar un dato en un nodo
        r = self.raiz                   # r == el nodo raiz del arbol existente
        if r.n == 2*self.t-1:           # condicional que solo corre si el numero de datos dentro del nodo actual son iguales al num max permitido de datos dentro de 1 nodo
            s = Nodo(self.t)            # s == un nuevo nodo
            self.raiz=s                 # reemplaza los datos que estan dentro de la raiz utilizando la lista vacia que se creo con la variable s (el nuevo nodo)
            s.hoja = 0                  # 
            s.n = 0
            s.hijos[1] = r
            self.bTreeSplitChild(s,1)
            self.bTreeInsertNonFull(s,k)
        else:
            self.bTreeInsertNonFull(r,k)
            
    def bTreeSplitChild(self,x,i):      # funcion para separar o dividir un nodo que esta lleno con datos y se necesita separar (supera el numero max de datos permitidos en un nodo)
        z = Nodo(self.t)                # z == nodo nuevo
        y = x.hijos[i]                  # y == 
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
   

# --- CODIGO PARA CORRER EL PROGRAMA ---

BT = ArbolB(2)
actual = BT.bTreeCreate()
print("Nodo Creado.")
print(BT.raiz.llaves)
BT.bTreeInsert(actual,111)
BT.bTreeInsert(actual,96)
BT.bTreeInsert(actual,84)
BT.bTreeInsert(actual,16)
# FECHA DE ULTIMA EDICION: 11/9/2021 9:28 AM