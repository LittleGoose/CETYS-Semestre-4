import random

def bubbleSort(arr):
    n = len(arr)
  
    #ciclo 'for' para realizar todas las iteraciones
    for i in range(n):
  
        #tomar el penultimo numero de elementos en la lista como 'j'
        for j in range(0, n-i-1):
  
            #condicional que checa los elementos desde la posicion 0 a n-i-1
            #Cambia el valor de los elementos si el 1ro es mayor que el 2do y pasa al siguiente
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
  
#codigo encargado de correr el programa
x=int(input('¿cuantos elementos en la lista?'))
arr = random.sample(range(1,100), x)
print('lista de elementos sin arreglar:\n' + str(arr))
print('Ciclos del Bubble Sort:')
bubbleSort(arr)