# modulo utilizado para crear la lista de elementos
import random
 
# funcion de Selection Sort
def SelectionSort(lista):
    
    #ciclo 'for' para hacer todas las iteraciones
    for i in range(len(lista)):
        
        #variable para encontrar el elemento minimo en el arreglo desordenado
        min_idx = i
        
        #ciclo 'for' para checar si el elemento en 'j' es mas grande que el elemento en 'min_idx'
        for j in range(i+1, len(lista)):
            
            #'if' que guarda el valor del elemento en 'min_idx' en la variable 'j' si el 1ro es mayor que el 2do
            if lista[min_idx] > lista[j]:
                min_idx = j
                
        #voltear el valor de los elementos en caso de que sea necesario    
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print(lista)
 
#parte de codigo necesario para correrlo
A = int(input('# de elementos en la lista: '))
lista = random.sample(range(1, 100), A)
SelectionSort(lista)
