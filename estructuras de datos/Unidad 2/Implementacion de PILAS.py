# Implementacion de pilas estaticas en LISTAS

# ESTRUCTURA DE PROGRMA---
class pila():
    def __init__(self, size):
        self.lista = []
        self.size = size
        self.top = -1
    
    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def IsFull(self):
        if self.size == self.top + 1:
            return True
        else:
            return False
        
    def InsertElement(self, Item):  #Apilar
        if not self.IsFull():
            self.lista.append(Item)
            #self.lista.push(Item)
            self.top += 1       #+= 1 es lo mismo que self.top + 1
            
    def DeleteElement(self):  #Desapilar (solo el ultimo)
        if not self.IsEmpty():
            self.lista.pop(self.top)
            self.top -= 1
        
# CODIGO DE OPERACIONES---
p = pila(5)
print(p.IsEmpty())
p.InsertElement(50)
print(p.lista)