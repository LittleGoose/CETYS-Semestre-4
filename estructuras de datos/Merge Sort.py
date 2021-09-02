# Codigo para Merge Sort
# Equipo: Iram Abbud 033150

# Funion "random" necesaria para conseguir la lista
import random

# Funcion para Merge Sort
def MergeSort(arr):
    
    # Si la lista es mayor a 1 la funcion corre
    if len(arr) > 1:
 
        # Encuentra el punto medio del arreglo
        mid = len(arr)//2
 
        # Divide el arreglo en 2, usando "mid" como el punto de separacion
        L = arr[:mid]
        R = arr[mid:]
 
        # Aplicar Merge Sort a las 2 partes
        MergeSort(L)
        MergeSort(R)

        # Asignamos el numero inicial a las variables que usaremos
        i = j = k = 0
 
        # Funcion "while" que ordena los elementos 
        while i < len(L) and j < len(R):
            
            # Si el elemento de la izquierda es menor, lo coloca en su lugar de la lista
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            
            # Si no, coloca el elemento de la derecha
            else:
                arr[k] = R[j]
                j += 1
            
            # Con cada corrida, la posicion de la lista ordenada donde se agregara el nuevo elemento se cambia
            k += 1
 
        # Checar si todos los elementos estan en la lista
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Codigo para correr el programa e imprimir las listas desordenadas y ordenadas
k = int(input('-'*30 + '\n# de elementos en la lista: '))
lista = random.sample(range(1, 100), k)
print ("-"*5 + "\nLista desordenada: \n" +  str(lista))
MergeSort(lista)
print('-'*5 + '\nLista ordenada:\n'+str(lista)+'\n'+'-'*30)