#Proyecto Parcial 1 / Estructuras de Datos / Manejo e implementacion de Pilas

# CETYS UNIVERSIDAD, CAMPUS TIJUANA
# Jorge Axel Cruz Jimenez 31973, Eumir Iram Abbud Orozco 33150

#--- CLASE PILA ---
class pila():
    # CONSTRUCTOR DE LA PILA
    def __init__(self, size):
        self.list = []
        self.size = size
        self.top = -1

    # FUNCION PARA SABER SI LA PILA ESTA VACIA
    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # FUNCION PARA SABER SI LA PILA ESTA LLENA
    def IsFull(self):
        if self.size == self.top+1:
            return True
        else:
            return False

    # FUNCION QUE APILA UN ELEMENTO
    def Insert(self, value):
        if not self.IsFull():
            self.list.append(value)
            self.top+=1

    # FUNCION PARA QUITAR EL ELEMENTO EN LA CIMA DE LA PILA (DESAPILAR)
    def Unstack(self):
        if not self.IsEmpty():
            self.list.pop(self.top)
            self.top-=1

    # FUNCION PARA OBTENER EL ELEMENTO QUE ESTA EN LA CIMA DE LA PILA
    def GetTop(self):
        if not self.IsEmpty():
            top = self.list[-1]
            return top

#---VARIABLES---
# POSICION DEL PRIMER ERROR EN LA CADENA
error_index = 0
# MENSAJE QUE INGRESA EL USUARIO Y CHECA EL PROGRAMA
input_string = input("enter some string:  ")
# VARIABLE CON EL NUMERO DE CARACTERES EN EL MENSAJE
stringLength = len(input_string)
# INSTACIA PARA EL MANEJO DE LA CLASE PILA (PARA VALIDAR '(', '[', '{' )
stack = pila(stringLength)
# INSTANCIA PARA EL MANEJO DE LA CLASE PILA (PARA VALIDAR ')', ']', '}' )
stack2 = pila(stringLength)
# BANDERA PARA EL OUTPUT
successFlag = True

# --- CODIGO PARA CORRER EL PROGRAMA ---
# EL CICLO RECORRE CADA CARACTER DE LA CADENA INTRODUCIDA
for i in range(0,stringLength):
    # SI EL CARACTER ES UN (, [ o {, SE AGREGA A LA PILA
    if input_string[i] == "(" or input_string[i] == "[" or input_string[i] == "{":
        stack.Insert(input_string[i])
        if not stack.IsEmpty():
            error_index = i
    
    # CASO CONTRARIO, DEBE CHECAR EL RESTO DE LOS CARACTERES
    else:
        # SI EL CARACTER NO ES UN PARENTESIS, CORCHETE O LLAVE ABIERTO, ENTONCES DEBE SER UNO CERRADO U OTRO CARACTER
        if input_string[i] == ")" or input_string[i] == "]" or input_string[i] == "}":
            stack2.Insert(input_string[i])

        # SE OBTIENE EL ELEMENTO EN LA CIMA DE LA PILA Y SE HACE LA COMPARACION CON EL ELEMENTO SIGUIENTE
        current_char = stack.GetTop()
        current_char2 = stack2.GetTop()
        
        # SE REALIZAN COMPARACIONES DEPENDIENDO DEL CARACTER QUE TENGA GUARDADO LA VARIABLE ('(', '[', o '{')
        # SI LOS VALORES COMPARADOS TERMINAN SIENDO UN USO DE PARENTESIS CORRECTAMENTE, NO HAY ERROR
        # SI NO HAY ERROR, ENTONCES REMUEVE ESE ELEMENTO DE LA PILA
        # CASO CONTRARIO REVISA SI ES UN PARENTESIS O LLAVE CERRADOS Y DE SER ASI, MARCA ERROR
        # EN CASO DE QUE LA VARIABLE "SuccesFlag" MARQUE FALSO (SEA UN ERROR), SE GUARDA SOLAMENTE LA POSICION DONDE SE GENERA EL PRIMER ERROR
        
        if current_char == '(' or current_char2 == ')':
            if current_char == "(" and current_char2 == ")" and not stack.IsEmpty():
                stack.Unstack()
                stack2.Unstack()
            else:
                if input_string[i] == "}" or input_string[i] == "]" or current_char2 == ")":
                    error_index = i
                    successFlag = False
                    break
        if current_char == '[' or current_char2 == ']':
            if current_char == "[" and current_char2 == "]" and not stack.IsEmpty():
                stack.Unstack()
                stack2.Unstack()
            else:
                if input_string[i] == ")" or input_string[i] == "}" or current_char2 == "]":
                    error_index = i
                    successFlag = False
                    break
        if current_char == '{' or current_char2 == '}':
            if current_char == "{" and current_char2 == "}" and not stack.IsEmpty():
                stack.Unstack()
                stack2.Unstack()
            else:
                if input_string[i] == ")" or input_string[i] == "]" or current_char2 == "}":
                    error_index = i
                    successFlag = False
                    break


# SI EN LA PILA HAY AL MENOS 1 ELEMENTO, SIGNIFICA QUE EXISTE AL MENOS 1 ERROR, POR LO TANTO SE IMPRIME LA POSICION DEL PRIMER ERROR
# SI LA PILA ESTA VACIA, SIGNIFICA 2 COSAS:
### a) SE HICIERON LAS COMPARACIONES CORRECTAS Y TODOS LOS PARENTESIS, CORCHETES Y LLAVES FUERON CERRADOS CORRECTAMENTE Y NO HAY ERRORES
### b) LA CADENA CAPTURADA NO POSEE NINGUN PARENTESIS, CORCHETE O LLAVE. POR LO TANTO NO HAY ERRORES Y OUTPUT ES CORRECTO
## POR LO TANTO LA BANDERA DEL SUCCESS SE ACTUALIZA SI PASAN ALGUNAS DE ESTAS CONDICIONES Y EL RESULTADO SE IMPRIME
## DEPENDIENDO DEL ESTADO DE LA BANDERA

if not successFlag:
    print(error_index+1)
else:
    print("Success")

### ULTIMA MODIFICACIÓN: 18/SEPTIEMBRE/2021 @ PST 7:19 PM