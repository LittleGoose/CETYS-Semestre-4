# Implementacion de QUEUEs usando listas

# ESTRUCTURA DEL PROGRAMA ----
class queue():
    def __init__(self):
        self.lista = []

    def isEmpty(self):
        if len(self.lista) == 0:
            return True
        else:
            return False
    
    def EnQueue(self, Item):
        self.lista.insert(0, Item)
        
    def DeQueue(self):
        if not self.isEmpty():
            self.lista.pop()
            
    def Front(self):
        if not self.isEmpty():
            return self.lista[len(lista)-1]
    
# CODIGO DE OPERACIONES ----
q = queue()
print('-'*10 + '\n' + str(q.isEmpty()))
q.EnQueue(3)
q.EnQueue('Indigo')
q.EnQueue(False)
print(q.lista)
q.DeQueue()
print(q.lista)
#print(f'{q.Front}') NO LOGRO HACER QUE FRONT FUNCIONE
    
        