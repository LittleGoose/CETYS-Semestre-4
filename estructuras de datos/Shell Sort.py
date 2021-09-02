# Codigo para Merge Sort
# Equipo #7: Axel Cruz 31973, Ivannia Gomez 27814, Iram Abbud 033150

# Funion "random" necesaria para conseguir la lista
import random
import math


def ShellSort(arr):
  
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = math.floor(n/2)
    print(n , ",", gap)
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
  
        for i in range(gap,n):
  
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
  
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
  
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap /= 2
        
# Codigo para correr el programa e imprimir las listas desordenadas y ordenadas
k = int(input('-'*30 + '\n# de elementos en la lista: '))
lista = random.sample(range(1, 100), k)
print ("-"*5 + "\nLista desordenada: \n" +  str(lista))
ShellSort(lista)
print('-'*5 + '\nLista ordenada:\n'+str(lista)+'\n'+'-'*30)