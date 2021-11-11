# META 3.1 | B-Tree

# INTEGRANTES
# Stephenie Gonzalez | 33892
# Iram Abbud | 33150
# David Roldan | 27292

# EJERCICIO | Implementar un codigo del arbol B

class Nodo:                             # Creacion de clase NODO
    
    def __init__(self, t):              # Inicializador de la clase, t == cantidad minima de datos dentro de un nodo
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

    def bTreeInsert(self, k):           # funcion para insertar un dato en un nodo
        r = self.raiz                   # r == el nodo raiz del arbol existente
        if r.n == 2*self.t:             # condicional que solo corre si el numero de datos dentro del nodo actual son iguales al num max permitido de datos dentro de 1 nodo + 1 (que 
                                        # significa que esta ocupando el espacio del dato invisible)
            s = Nodo(self.t)            # s == un nuevo nodo
            self.raiz=s                 # reemplaza los datos que estan dentro de la raiz utilizando la lista vacia que se creo con la variable s (el nuevo nodo)
            s.hoja = 0                  # indica que s es el nodo padre de otro nodo (probablemente r)
            s.n = 0                     # indica que hay 0 datos guardados dentro de este nodo
            s.hijos[1] = r              # indica que la posicion del primer hijo del nodo "s" es el nodo "r" ("r" era el nodo raiz original)
            self.bTreeSplitChild(s,1)       # llama a la funcion bTreeSplitChild utilizando el nodo "s" (el nodo padre de r), y #1
            self.bTreeInsertNonFull(s,k)    # llama a la funcion bTreeInsertNonFull utilizando el nodo "s" y "k" == el numero que se quiere insertar
        else:
            self.bTreeInsertNonFull(r,k)    # llama a la funcion bTreeInserNonFull utilizando el nodo raiz y "k" == el numero que se quiere insertar
            
    def bTreeSplitChild(self,x,i):      # funcion para separar o dividir un nodo que esta lleno con datos y se necesita separar (supera el numero max de datos permitidos en un nodo)
        z = Nodo(self.t)                # z == nodo nuevo
        y = x.hijos[i]                  # y == los datos del hijo con la posicion del contador "i" (#1) del nodo que utilizamos para llamar esta funcion ("x")
        z.hoja = y.hoja                 # se guarda el num de hoja en el nuevo nodo utilizando el num de hoja del nodo que guardamos en "y"
        z.n = self.t-1                  # se guarda el num actual de datos que estan dentro del nodo
        
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
            while (i >= 1) and (k < x.llaves[i-1]):
                x.llaves[i] = x.llaves[i-1]
                i = i-1
            x.llaves[i] = k
            x.n = x.n+1
        else:
            while (i >= 1) and (k < x.llaves[i]):
                i = i-1
            i = i+1
            if x.hijos[i].n == 2*self.t-1:
                self.bTreeSplitChild(x,i)
                if k > x.llaves[i]:
                    i = i+1
            self.bTreeInsertNonFull(x.hijos[i], k)
        
    def bTreeSearch(self,nodo,k):                           # funcion para buscar las llaves del nodo / "nodo" == el nodo deseado y "k" == el dato 
        x = nodo                                            # x == nodo donde se realizara la busqueda (explicacion implicita)
        i = 1                                               # "i" == contador
        while i <= x.n and k > x.llaves[i]:                 # bucle que corre mientras el contador sea menor o igual al numero de datos que estan en el nodo Y el 
                                                            # dato buscado sea mayor que el dato actual (que este en la posicion del contador)
            i = i+1                                         # se le suma 1 al contador
        print(f"i, Llaves del nodo: {i}, {x.llaves[i]}")    # imprime el nodo y el numero, indicando que el numero buscaod si existe dentro del arbol 
        if i <= x.n and k == x.llaves[i]:                   # condicional que corre si el contador es menor o igual al numero de datos que estan en el nodo Y el 
                                                            # numero buscado es igual al dato que esta en la posicion del contador
            return(x,i)                                     # regresa el nodo y el numero actual del contador
        else:                                               # si el condicional pasado no corre, este si
            if x.hoja == 1:                                 # si el numero de hoja es igual a 1
                return None                                 # No existe
            else:                                           # si el numero de hoja no es 1
                return self.bTreeSearch(x.hijos[i],k)       # Leer el disco

    def imprimeNodo(self,nodo):                     # funcion para imprimir los datos de 1 nodo especifico
        for i in range(0,2+self.t,1):               # bucle que empieza en la posicion 0 y recorre todos los datos dentro del nodo
            if nodo.llaves[i] != None:              # condicional que corre si el dato en la posicion "i" dentro del nodo NO es None
                print(nodo.llaves[i], end=' ')      # imprime el valor del nodo con un espacio de separacion
   

# --- CODIGO PARA CORRER EL PROGRAMA ---

BT = ArbolB(2)
BT.bTreeCreate()
print("Nodo Creado.")
BT.bTreeInsert(111)
BT.bTreeInsert(96)
BT.bTreeInsert(84)
BT.bTreeInsert(16)
BT.bTreeInsert(6)
print(BT.raiz.llaves)
print("\n")
print(BT.bTreeSearch(BT.raiz, 96))

# FECHA DE ULTIMA EDICION: 11/10/2021 11:28 PM