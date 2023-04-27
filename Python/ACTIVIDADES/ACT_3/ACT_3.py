# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:03:24 2023

@author: Santiago Defaz
"""

def es_bisiesto(anio):

    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True
print(es_bisiesto(2000))
