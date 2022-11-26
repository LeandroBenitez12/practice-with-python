"""
largo = int(input("introduce el largo del rectangulo(m): "))
ancho = int(input("introduce el ancho del rectangulo(m): "))
area = largo*ancho
perimetro = (largo + ancho ) * 2

print("el perimetro del triangulo es: " + str(perimetro))
print("el area del triangulo es: " + str(area) )

valor1 = int(input("introduzca el primer valor entero: "))
valor2 = int(input("introduzca el segundo valor entero: "))

if(valor1 == valor2):
    print(" Son iguales")
elif not (valor1 > valor2) : 
    print(str(valor1) + " es menor a " + str(valor2))
else:
    print(str(valor1) + " es mayor a " + str(valor2))

print ("provide the dates of the book")
name = input(" enter the name of the book: ")
cost = float(input(" enter the cost of the book: "))
shiping = bool(input(" indicate if the shipings is free(True/False): "))

print("the name is: " + name)
print("the cost is :" + str(cost)) 
print("the shipings is free(True/False):" + str(shiping))   

#ARGS

import re
from unittest import result


def Suma(*args) -> int :
    resultado = 1
    for numero in args :
        resultado *= numero
    return resultado
Result = Suma(4,5,10)
print("El resultado es: " + str(Result))
  """
  #def recursivas

from unittest import result


def factorial(numero):
    resultado = 0
    for num in numero:
        if num > 0:
            resultado = numero - 1
    return resultado
resultado = (factorial(3))
print(resultado)