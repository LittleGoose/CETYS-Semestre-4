#Practica 1.4 Pilas -Palindromos
#Iram Abbud, Gustavo Lopez y Gabriela Sánchez

# Modulo necesario para poder usar la funcion de ascii_lowercase mas adelante
import string

# ESTRUCTURA DE CODIGO
class pilas():
    def __init__(self, size):
        self.lista = []
        self.size = size
        self.top = -1

    def IsEmpty(self): #revisa que la lista no esta vacia
        if self.top == -1:
            return True
        else:
            return False
    
    def IsFull(self): #revisa que la lista no este llena
        if self.size == self.top + 1:
            return True
        else:
            return False

    def InsertElement(self, item): #se agrega un Item a la lista
        if not self.IsFull():
            self.lista.append(item)
            self.top =+ 1 #El ultimo elemento se agrega 1, porque la lista ya tiene 1 dato mas

# CORRER PROGRAMA
def is_palindrome(s):
    
    list = set(string.ascii_lowercase)
    s = s.lower() #hace que todo sea en minusculas
    s = ''.join([char for char in s if char in list]) #.join junta 
    print(s)
    return s == s[::-1] 

palabra = str(input('-'*30+"\nIngrese su palabra: "))

p = pilas(5)
p.InsertElement(palabra)    
x = p.IsEmpty()

if palabra == '':
    x = True

    
if x == True:
    print('-'*5+'\nNo hay palabra registrada\n'+'-'*30)
else:
    ans = is_palindrome(palabra)
    if ans: 
        print('-'*5+f"\nLa palabra/frase '{palabra}' SI es un palindromo\n"+'-'*30)
    else:
        print('-'*5+f"\nLa palabra/frase '{palabra}' NO es un palindromo\n"+'-'*30)