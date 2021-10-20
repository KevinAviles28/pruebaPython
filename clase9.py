#!/usr/bin/python
# -*- coding: utf-8 -*-
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 11,2 g y cada muñeca 7,5 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

"""pesoPayaso= 11.2
pesoMunieca = 7.5

while True:
   try: 
       numeroPayaso= int(input("Ingrese la cantidad de Payasos vendidos en el ultimo pedido\n"))
   except ValueError:
       print("Error debe de ingresar la cantidad de payasos")
   else:
        break

while True:
    try:
        numeroMunieca= int(input("Ingrese la cantidad de Muñecas vendidas en el ultimo pedido\n"))
    except ValueError:
        print("Error debe de ingresar la cantidad de muñecas")
    else:
        break
pesoTotalPayaso= numeroPayaso*pesoPayaso
pesoTotalMunieca= numeroMunieca*pesoMunieca

pesoTotal= round(pesoTotalPayaso+pesoTotalMunieca,)

print("El peso total de los payaso y las muñecas en el ultimo pedido es de:",pesoTotal,"Kg")"""



#Se pide obtener informar que tipo de triángulo es. Sabiendo que ingresan 3 datos correspondientes al largo de cada lado. Recordar: el triángulo equilátero tiene los 3 lados iguales, el isósceles 2 lados iguales y el escaleno los 3 lados distintos.


"""primerLado= int(input("Ingrese el primer lado del triangulo: "))
segundoLado= int(input("Ingrese el segundo lado del triangulo: "))
tercerLado= int(input("Ingrese el tercer lado del triangulo: "))
lados=[primerLado,segundoLado,tercerLado]
contador=0"""
lado1=0
lado2=0
lado3=0
def ingresoLado(lado):
 while True:
    try:
        lado +=int(input("Ingrese la medidad del lado en cm: "))
        print (lado)
    except ValueError:
        print("Debe de ingresar un lado")
    else:
        if lado <= 0:
            print("Debe de ser un numero positivo o mayor a 0")
        else:
            break



ingresoLado(lado1)
ingresoLado(lado2)
ingresoLado(lado3)



print(lado1,lado2,lado3)

if lado1==lado2 and lado1==lado3:
        print("El triagulo es un equilatero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("El triangulo es un isósceles")
else:
        print("el triangulo es un escaleno")
    

"""
while True:
    try:
        lado1 = int(input("ingrece la medida del lado 1 en cm: "))
    except ValueError:
        print("Debe de ingresar un numero")
    else:
        if lado1 <= 0:
            print("Debe de ser un numero positivo o mayor a 0")
        else:
            break

while True:
    try:
        lado2 = int(input("ingrece la medida del lado 2 en cm: "))
    except ValueError:
        print("Debe de ingresar un numero")
    
    else:
        if lado2 <= 0:
            print("Debe de ser un numero positivo o mayor a 0")
        else:
            break

while True:
    try:
        lado3 = int(input("ingrece la medida del lado 3 en cm: "))
    except ValueError:
        print("Debe de ingresar un numero")
    
    else:
        if lado3 <= 0:
            print("Debe de ser un numero positivo o mayor a 0")
        else:
            break"""




