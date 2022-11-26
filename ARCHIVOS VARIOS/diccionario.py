from cgitb import text
from typing import TextIO


diccionario = {
    "programar": "Dar las instrucciones necesarias a una máquina o aparato para que realice su función de manera automática",
    "POO" : "Programacion Orientada a Objetos",
    "MVC" : "Modelo vista controlador"
}   
print(diccionario["POO"])

conversor = {
    "0" : "cero",
    "1" : "uno",
    "2" : "dos",
    "3" : "tres",
    "4" : "cuatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "siete",
    "8" : "ocho",
    "9" : "nueve"
}
dato = input("ingrese un numero:  ")
textoFinal = " "
for letra in dato:
    textoFinal += conversor[letra] + " "

    
print(textoFinal)
