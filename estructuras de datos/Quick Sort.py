# Codigo para Quick Sort
# Equipo #6: Daniel Garcia 26305, Esteban Rodarte 19457, Iram Abbud 33150

# Se utiliza la funcion de "random" para poder crear una lista con integrales aleatorios
import random

# Funcion para Quick Sort
def QuickSort(lista,l,r):
    
    # Si la lista tiene solo 1 elemento, la regresa sin hacer calculos
    if len(lista) == 1:
        return lista
    
    # Si el valor del indice es igual o mayor al numero maximo de elementos en la lista, la funcion acaba
    if l >= r:
        return
    
    # Se crean las particiones de la lista
    m = Partition(lista,l,r)
    
    # Se vuelve a utilizar la funcion de Quick Sort, con las particiones respectivas
    QuickSort(lista,l,m)
    QuickSort(lista,m+1,r)

# Funcion para el orden de las particiones
def Partition(lista,l,r):
    
    # valor del pivote
    pivote = lista[l]
    
    # indice que indica que valor se utiliza para cambiar
    j = l
    
    for i in range(l+1, r):
        
        if lista[i] <= pivote:
            
            # incrementar el indice
            j = j + 1
            lista[j], lista[i] = lista[i], lista[j]
    
    lista[l], lista[j] = lista[j], lista[l]

    return j


k = int(input('-'*30 + '\n# de elementos en la lista: '))
lista = random.sample(range(1, 100), k)
print ("-"*5 + "\nLista desordenada: \n" +  str(lista))
QuickSort(lista, 0, k)
print('-'*5 + '\nLista ordenada:\n'+str(lista)+'\n'+'-'*30)