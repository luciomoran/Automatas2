# Nombre: Circunferencia.py
# Objetivo: Calcular el área y diámetro de una circunferencia e importar la librería "Math"
# Autor: Lucio David Morán Brizuela
# Fecha: 1 de julio 2019

import math as mat
import os

def calcularArea(r):
    area = mat.pi*(mat.pow(r,2))
    return area

def calcularDiametro(d):
    diam = d*2
    return diam


def main():
    ciclo = True
    while (ciclo == True):
        print("-- Script para calcular el área de circunferencia --")
        radio = float(input("Introduce el valor del radio: "))
        # Invocar un método
        print("El área es: ", calcularArea(radio))
        print("El diámetro es: ", calcularDiametro(radio))
        
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
