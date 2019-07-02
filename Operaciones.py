# Nombre: Operaciones.py
# Objetivo: Mostrar como trabajan las operaciones en Python
# Autor:
# Fecha: 29 de junio 2019


#-------------------------------
# Funcion para sumar dos enteros
#-------------------------------
def suma(num1, num2):
    return num1+num2


#-------------------------------
#Funcion para restar dos números
#-------------------------------
def resta(num1, num2):
    return num1-num2


#------------------------------------
#Funcion para multiplicar dos números
#-----------------------------------
def mult(num1, num2):
    return num1*num2


#--------------------------------
#Funcion para dividir dos números
#--------------------------------
def divide(num1, num2):
    return num1/num2


#---------------------------------
#Funcion para comparar dos enteros
#---------------------------------
def compara(num1, num2):
    if(num1>num2):
        print("El mayor es num1: ", num1)

    elif(num2>num1):
        print("El mayor es num2: ", num2)

    else:
        print("Los numeros son iguales: ", num1, ", ", num2)


#------------------------------------
#Función para hacer un ciclo con for
#------------------------------------
def cuenta(num1, num2):
    for i in range(num1, num2):
        print("Valor de i: ", i)


# Función main
def main():
    ciclo = True
    while (ciclo == True):
        print("--Operaciones Básicas con Enteros--")
        print("\n")
        n1=int( input("Introduce numero A: "))
        n2=int( input("Introduce numero B: "))
        print("\n")

        #Invocamos las funciones
        print("La suma es: ", (suma(n1,n2)))
        print("La resta es: ", (resta(n1,n2)))
        print("La mutiplicación es: ", (mult(n1,n2)))
        print("La división es: ", (divide(n1,n2)))
        #Invocamos el método compara
        compara(n1, n2)

        print("\n")
        cad = input("¿Otro cálculo (s/n)? ")
        if (cad == "S" or cad == "s"):
            ciclo = True
        else:
            ciclo = False


if __name__ == "__main__":
    main()


