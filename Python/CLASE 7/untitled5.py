# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:22:50 2023

@author: ADM-DGIP
"""

class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad        
    def presentarse(self):
        print(f"¡Hola, mi nombre es {self.nombre} y tengo {self.edad} años!")        
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Mi nombre ha sido cambiado a {self.nombre}.")    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
          return True
        else:
            return False             
        
persona1=persona("Juan", 16)
persona2=persona("Ana",36)
persona3=persona("Luis",45)
persona4=persona("Santiago",25)
persona1.presentarse()
persona2.presentarse()  
persona3.presentarse()
persona4.presentarse()  
persona1.cambiar_nombre("Ana")

