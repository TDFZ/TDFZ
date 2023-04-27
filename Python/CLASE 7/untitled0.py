# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:01:12 2023

@author: ADM-DGIP
"""

def ingresar_entero():
    lmin=input("Ingrese límite mínimo: ")
    lmax=input("Ingrese límite máximo: ")
    num_str = input("Ingrese un número entero: ")
    lim1=int(lmin)
    lim2=int(lmax)   
    num = int(num_str)
    try: 
        
        if lim1<= num <= lim2
            return num
        else:
            print("El valor debe estar en el rango {lim1} y {lim2}")
    except ValueError:
        print("Debe ingresar un número válido.")
        
mi_numero = ingresar_entero()
print("El número ingresado es:", mi_numero)