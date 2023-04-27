# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:25:53 2023

@author: ADM-DGIP
"""

def crealista(n):
    lista=[]
    for item in range(1,n+1,1):
        lista.append(item)
    return lista

print(crealista(10))