# CODIGO PARA ARBOL BINARIO Y AVL
# IRAM OROZCO 33150

# Clase nodo
class Nodo():
    
    # Inicializador
    def __init__(self, value = None, parent = None, is_root = False, is_left = False, is_right = False):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.root = is_root
        self.is_left = is_left
        self.is_right = is_right
        self.height = 1

    # Altura de un nodo          
    def get_height(self, cur_nodo):
        if cur_nodo == None:
            return 0
        return cur_nodo.height

    # Nodo mas alto
    def taller_child(self, cur_nodo):
        left = self.get_height(cur_nodo.left)
        right = self.get_height(cur_nodo.right)
        if left >= right:
            return cur_nodo.left 
        else:
            return cur_nodo.right

    # Insepccion de Insercion
    def _inspect_insertion(self, cur_nodo, path = []):
        if cur_nodo.parent == None:
            return
        path = [cur_nodo] + path
        left_height = self.get_height(cur_nodo.parent.left)
        right_height = self.get_height(cur_nodo.parent.right)
        print(f'altura, izq y derecha: {left_height} y {right_height}')
        if abs(left_height - right_height) > 1:
            path = [cur_nodo.parent] + path
            self._rebalance_nodo(path[0], path[1], path[2])
            return
        new_height = 1 + cur_nodo.height
        if new_height > cur_nodo.parent.height:
            cur_nodo.parent.height = new_height
        self._inspect_insertion(cur_nodo.parent, path)
        

# Rotacion a la derecha
def _right_rotate(self,z):
    sub_root = z.parent
    y = z.left
    t3 = y.right
    z.parent = y
    z.left = t3
    if t3 is not None:
        t3.parent = z
    y.parent = sub_root
    if y.parent == None:
        self.root = y
    else:
        if y.parent.left == z:
            y.parent.left = y
        else:
            y.parent.right = y
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))    
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))    

# Rotacion a la izquierda  
def _left_rotate(self,z):
    sub_root = z.parent
    y = z.right
    t2 = y.left
    y.left = z
    z.parent = y
    z.right = t2
    if t2 is not None:
        t2.parent = z
    y.parent = sub_root
    if y.parent == None:
        self.root = y
    else:
        if y.parent.left == z:
            y.parent.left = y
        else:
            y.parent.right = y
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))    
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))    

# Balancear nodos
def _rebalance_nodo(self, z, y, x):
    if y == z.left and x == y.left:
        self._right_rotate(z)
    elif y == z.left and x == y.right:
        self._left_rotate(y)
        self._right_rotate(z)
    if y == z.right and x == y.right:
        self._left_rotate(z)
    elif y == z.right and x == y.left:
        self._right_rotate(y)
        self._left_rotate(z)
    else:
        raise Exception('La configuracion z,y,x del nodo no fue reconocida')