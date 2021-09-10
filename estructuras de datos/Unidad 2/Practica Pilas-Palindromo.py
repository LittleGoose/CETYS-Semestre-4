# Practica 1.4 Pilas -Palindromos
# Iram Abbud, Gustavo Lopez y Gabriela Sánchez

# Modulo necesario para poder usar la funcion de ascii_lowercase mas adelante
import string

# ESTRUCTURA DE CODIGO
class pilas():                # Inicializacion la clase pilas con sus metodos y atributos
    def __init__(self, size): # Size se utiliza para ver si la lista esta llena y confirmar si se puede insertar un elemento
        self.lista = []       # La lista inicialisada y vacia
        self.size = size      # Tamaño maximo de la lista
        self.top = -1         # Minimo y maximo de la lista, utilizado para checar que la lista no este vacia

    def IsEmpty(self):        # Revisa que la lista no esta vacia
        if self.top == -1:    # Si la lista esta en 0 esta vacia y regresa el valor booleano True
            return True
        else:
            return False
    
    def IsFull(self):         # Revisa que la lista no este llena
        if self.size == self.top + 1:   # Si el ultimo valor de la lista es igual a size, la lista esta llena y regresa True
            return True
        else:
            return False

    def InsertElement(self, item):      # Se agrega un Item a la lista
        if not self.IsFull():           # Checa que la lista no este llena
            self.lista.append(item)     # append sirve para agreguar el item a la lista
            self.top =+ 1               # El ultimo elemento se agrega 1, porque la lista ya tiene 1 dato mas

# CORRER PROGRAMA
def is_palindrome(s):         # Se crea una funcion para checar si la palabra/frase es palindromo
    list = set(string.ascii_lowercase)      # Se crea una variable donde se guarda la palabra en minusculas para compararla despues
    s = s.lower()                           # Hace que la palabra original todo sea en minusculas
    s = ''.join([char for char in s if char in list]) #.join junta los caracteres, eliminando los espacios vacios 
    return s == s[::-1]                     # Revisa que la palabra original sea igual si esta al reves 
                                            # los doble puntos iniciales indican que empieza a verificar la palabra de derecha a izquierda

palabra = str(input('-'*30+"\nIngrese su palabra: ")) # Se le pide al usuario que ingrese una palabra o frase

p = pilas(5)                # Se inicializa la clase pilas con su tamaño de lista (size)
p.InsertElement(palabra)    # se agrega la palabra a la lista por el metodo de la clase pilas
x = p.IsEmpty()             # variable que guarda el valor de el metodo IsEmpty

if palabra == '':           # Declaracion que checa si la lista esta vacia, ya que si el usuario pone un
    x = True                # 'Enter' la variable da resultado de 'Falso' cuando deberia ser 'Verdadero'

    
if x == True:                                                   # Si x es 'Verdadero' significa que la lista esta vacia
    print('-'*5+'\nNo hay palabra/frase registrada\n'+'-'*30)   # Se imprime que no hay palabra o frase registrada
else:                                                           # Si x es 'Falso' la lista no esta vacia
    ans = is_palindrome(palabra)                                # Mandamos a llamar a la funcion que checa si la palabra/frase es un palindromo
    if ans:                                                     # Si es un palindromo se imprime lo siguiente
        print('-'*5+f"\nLa palabra/frase '{palabra}' SI es un palindromo\n"+'-'*30)
    else:                                                       # Si NO es un palindromo se imprime lo siguiente       
        print('-'*5+f"\nLa palabra/frase '{palabra}' NO es un palindromo\n"+'-'*30)
        
# Programa elaborado por: Gabriela Sanchez, Tijuana Baja California Norte, 9/9/2021