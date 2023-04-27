# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:25:20 2023

@author: ADM-DGIP
"""

lista=[1,5.3,"Hola",True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
tupla=(1,5.3,"Hola",True)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
lista[3]="R1"
del lista[3]
print(lista)
tupla[3]="R1"
del tupla[3]
print(tupla)