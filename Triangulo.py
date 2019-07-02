# Nombre: Circunferencia.py
# Objetivo: Calcular el área y diámetro de una circunferencia e importar la librería "Math"
# Autor: Lucio David Morán Brizuela
# Fecha: 1 de julio 2019

#---------------------------------------------
#Función para identificar el tipo de triángulo
#--------------------------------------------
import os


def identifica(l1, l2, l3):
    # Equilátero
    if(l1 == l2 and l1 == l3):
        print("El triángulo es EQUILATERO -> ", l1, ", ", l2, ", ", l3)
   
    # Escaleno
    elif(l1 != l2 and l1 != l3):
        print("El triángulo es ESCALENO -> ", l1, ", ", l2, ", ", l3)

    # Isóceles
    elif(l1 == l2 and l1 != l3):
        print("El triángulo ISÓSCELES -> ", l1, ", ", l2, ", ", l3)

def main():
    ciclo = True
    while (ciclo == True):
        print("---- Script para identificar triángulos ----")
        lado1 = float(input("Introduce el lado 1: "))
        lado2 = float(input("Introduce el lado 2: "))
        lado3 = float(input("Introduce el lado 3: "))
        # Invocar a la función
        identifica(lado1, lado2, lado3)

        print("\n")
        resp = input("¿Desea hacer algo más? (s/n): ")
        if (resp == "S" or resp == "s"):
            ciclo = True
        else:
            ciclo = False

        # Borra pantalla
        os.system("cls")
    else:
        print("FIN DEL PROGRAMA...")


if __name__ == "__main__":
    main()