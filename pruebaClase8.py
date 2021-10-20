
##!/usr/bin/env python     # por si no instalamos python
# -*- coding: utf-8 -*-     ## para aceptar caracteres especiales

a=0
b=0
def suma(a,b):
    print("El resultado de la operacion es",a+b) 

def resta(a,b):
    print("El resultado de la operacion es",a-b) 

def multiplicacion(a,b):
    print("El resultado de la operacion es",a*b) 

def divicion(a,b):
    print("El resultado de la operacion es",a/b) 

while True:

    while True:
        try:
         a=int(input("Ingrese el primer numero:\n "))
        except ValueError:
         print("Error debe de ingresar un valor entero ") 
        else:
            break

    while True:
        try:
         b=int(input("Ingrese el segundo numero:\n "))
        except ValueError:
         print("Error debe de ingresar un valor entero ") 
        else:
            break
    print("Que calculo quiere para:",a,"y",b,"?")    
    operacion = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))

    try: 
        if(operacion =="1"):
            suma(a,b)
            break
        elif operacion == "2":
            resta(a,b)
            break
        elif operacion == "3":
            multiplicacion(a,b)
            break
        elif operacion == "4":
            divicion(a,b)
            break
        else:
            print("Error debe de ingresar las opciones del 1 al 4")
    except ZeroDivisionError:
            print("ERROR no puede dividir por 0")   
    
    


    
    
"""
while True:
    try:
        b=int(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Error debe de ingresar un valor entero ")
        print(a,b,operacion)    
   """         
            



