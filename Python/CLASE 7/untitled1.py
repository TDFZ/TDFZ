# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:31:55 2023

@author: ADM-DGIP
"""

def ingresar_numero_en_rango(minimo, maximo):
    while True:
        num_str = input(f"Ingrese un número entero entre {minimo} y {maximo}: ")
        try:
            num = int(num_str)
            if minimo <= num <= maximo:
                return num
            else:
                print(f"El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
num = ingresar_numero_en_rango(1, 100)
print(f"El número ingresado es: {num}")
