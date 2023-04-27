# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:24:40 2023

@author: ADM-DGIP
"""

def fibonacci():
    n=int(input("Ingrese n para serie de Fibonacci: "))
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(n)
        