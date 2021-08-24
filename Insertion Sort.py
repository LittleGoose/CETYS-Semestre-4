#Codigo para Insertion Sort
#Gabriela Sanchez Alcaraz 33229, Gustavo Lopez 33225, Iram Abbud 33150, Stephanie Gonzalez 33892

#se utiliza la funcion de "random" para poder crear una lista con integrales aleatorios
import random

#se crea la funcion de insertion sort
def insertionSort(lista):
    
    #esto recorre el indice utilizado por lo largo que sea la lista
    for i in range(1, len(lista)):
        
        #key = variable para guardar el valor de i actual
        key = lista[i]
        #j = el valor que con el que key se va a comparar
        j = i-1
        
        #funcion que compara las variables 'key' y 'j' hasta que 'key' sea mayor que 'j'
        #esta funcion se mantiene activa mientras aun existan integrales que 'j' pueda utilizar
        while j >=0 and key < lista[j] :

        #se mueven los numeros guardados en las variables a la posicion que queremos
                lista[j+1] = lista[j]
                j -= 1
        lista[j+1] = key
        
        #se imprime cada iteracion de la lista para que se vea el proceso
        print(lista)

#funcion para correr el codigo
while True:
    
    #se le pide al usuario que ingrese cuantos numeros habra en la lista
    n = int(input('Numero de valores en la lista: '))
    
    #funcion 'if' que checa si la lista tiene un numero valido de elementos para poder correr
    #si es entre 1 y 50 el programa corre, si es otro valor se le dice al usuario que intente otra vez
    if 1<= n <=50:
        lista = random.sample(range(1, 100), n)
        print ("La lista desordenada: \n" +  str(lista))
        print('Pasos del Insertion Sort para ordenar la lista:')
        insertionSort(lista)
    else:
        print('El numero de valores debe ser entre 1 y 50, intente nuevamente\n')