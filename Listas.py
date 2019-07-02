# Nombre: Listas.py
# Objetivo: Muestra el funcionamiento de las listas en Python
# Autor: Lucio David Morán Brizuela
# Fecha: 2 de julio 2019

import os

#Declaramos de manera global la lista
lista=[]

#---------------------------------------------
#Función para agregar items a la lista
#--------------------------------------------
def agregarItem(dato):
    lista.append(dato)


#------------------------------------------------
#Función para borrar items de la lista
#------------------------------------------------
def eliminarItem(dato):
    if (dato in lista):
        lista.remove(dato)
        print("Dato ELiminado")
    else:
        print("El item NO existe en la lista...")

#------------------------------------------------
#Función para imprimir los elementos de la lista
#------------------------------------------------
def imprimirLista():
    j=0
    for i in lista:
        print("Item: ",j,", ", i)
        j = j+1


#Menu principal del programa
def main():
    ciclo = True
    while (ciclo == True):
        print("---Script para Trabajar con Listas---")
        print("1. Agregar elementos a la lista")
        print("2. Buscar un elemento en la lista")
        print("3. Modificar elementos a la lista")
        print("4. Borrar un elementos a la lista")
        print("5. SALIR")
        opcion= int(input("ELIJA UNA OPCION: "))
        
        print("\n")
        
        if(opcion == 1):
            item = input("Introduce un valor del elemento: ")
            agregarItem(item)
        elif (opcion == 2):
            print()
        elif (opcion == 3):
            print()
        elif (opcion == 4):
            item = input("Elige un elemento a borrar: ")
            eliminarItem(item)
        elif (opcion == 5):
            print("...FIN DEL PROGRAMA...")
            ciclo = False
        else:
            print("Selecciona un entero entre 1 y 5")
            print("\n")


if __name__ == "__main__":
    main()

