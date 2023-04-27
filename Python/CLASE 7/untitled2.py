# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:37:49 2023

@author: ADM-DGIP
"""

def ingresar_tres_valores():
    valor1 = input("Ingrese el primer valor: ")
    valor2 = input("Ingrese el segundo valor: ")
    valor3 = input("Ingrese el tercer valor: ")
    return (valor1, valor2, valor3)
valores = ingresar_tres_valores()
print("Los valores ingresados son:", valores)