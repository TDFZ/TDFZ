# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:44:23 2023

@author: ADM-DGIP
"""

def ingresar_numero_entero():
    limmin=input("Ingrese número mínimo: ")
    limmax=input("Ingrese número máximo: ")
    while True:       
        num_str = input(f"Ingrese un número entero entre {limmin} y {limmax}: ")
        try:
            num = int(num_str)
            lmax=int(limmax)
            lmin=int(limmin)
            if lmin <= num <= lmax:
                return num
            else:
                print(f"Ingrese un número entero entre {limmin} y {limmax}: ")
        except ValueError:
            print("Debe ingresar un número entero válido.")
num = ingresar_numero_entero()
print(f"El número ingresado es: {num}")