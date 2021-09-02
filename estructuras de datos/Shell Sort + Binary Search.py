# Codigo para Shell Sort + Binary Search
# Equipo #7: Iram Abbud 033150, Axel Cruz 31973, Ivannia Gomez 27814

# Funcion para correr Shell Sort
def ShellSort(arr):
    # Variable 'gap' creada para despues guardar
    # la distancia que se utiliza para comparar elementos
    gap = len(arr) + 1

    # Funcion 'while' que compara elementos, que corre mientras la distancia entre elementos comparados sea > 1
    while gap > 1:

        # distancia entre elementos se actualiza
        gap = gap // 2

        # Condicion para que el programa corra
        # Bandera para identificar si hubo cambia en la última corrida
        flag = True
        while flag:

            # Inmediatamente quitamos la condicion, asumiendo
            # que esta corrida sera la ultima
            flag = False

            # Variable para la posicion actual en la "lista ordenada"
            i = 0

            # funcion while que decide si aun se debe correr la comparacion entre elementos
            while i + gap <= len(arr) - 1:

                # Se comparan 2 elementos utilizando la distancia entre ellos (gap)
                # y si el 1ro es mayor se cambian de posicion
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]

                    # Como hubo cambio de elementos, asumimos que esta no es la ultima
                    # corrida necesaria, se activa la condicion para correr el programa de nuevo
                    flag = True

                # Se suma 1 a la variable de posicion
                i += 1
    return arr


# Funcion para Binary Search
def BinarySearch(arr, target):
    # Variables para poder buscar el numero pedido que determinar los límites de arreglo a buscar
    min = 0
    max = len(arr) - 1

    # Funcion while para buscar el numero utilizando min y max
    # Se realiza un ciclo sin parada hasta que los min>=max, por lo tanto no se encontro o se llega al número buscado
    while True:

        # Creamos una variable con la posicion media del arreglo que es nuestro intento actual
        guess = (min + max) // 2

        # Si esta posicion resulta tener el numero buscado termina el programa
        if arr[guess] == target:
            break
        # Si el numero en la posicion de nuestro intento es menor que el numero
        # buscado se suma 1 al rango minimo y se intenta otra vez
        elif arr[guess] < target:
            min = guess + 1
        # Si el numero de nuestro intento es mayor, se resta 1 al rango
        # maximo y se intenta otra vez
        else:
            max = guess - 1
        # Si el numero no se encuentra y se regresa un "No"
        # como respuesta a la funcion
        if min > max:
            return "No"
    return guess


# Se le pide al ususario el # de elementos en el arreglo
n = int(input("ingrese el # de elementos del arreglo: "))

# Funcion while que pide cuales elementos seran y checa si
# la cantidad coincide con los que ingreso el usuario en 'n'
while True:
    datos = list(map(int, input("Ingrese los numeros separandolos por un espacio: ").split()))
    # Imprimimos un error si la condicion fue seguida
    if len(datos) != n:
        print('Numero de datos incorrecto, intente otra vez!')
    else:
        break

# Imprimimos la lista ordenada
print(f"Lista ordenada: {ShellSort(datos)}")

# Funcion while para realizar el Binary Search
while True:
    # Pedimos el numero que se quiere buscar
    x = int(input("¿Que numero desea buscar? "))

    # Se implementa Binary Search
    buscar = BinarySearch(datos, x)

    # Si BinarySearch no encuentra el numero, se lo indica
    # al usuario y puede intentar otra vez
    if buscar == "No":
        print("Ese numero no existe en el arreglo")

    # Si encuentra el numero lo imprime junto con su posicion
    # en el arreglo y termina el programa
    else:
        print(f"el numero {x} se encuentra en la posicion {buscar + 1} del arreglo")
        break

# ÚLTIMA MODIFICACIÓN
# 9:55 el 2 de septiembre de 2021, por Iram Abbud
# linea 109