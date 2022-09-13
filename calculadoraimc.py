from os import device_encoding
from unittest import result
from xml.dom import minicompat

imc_minimo = 19
imc_medium2 = 25
imc_maximo = 25

peso = int(input("Ingrese su peso:  "))
alturaenCm = int(input("Ingrese su altura :  "))
alturaenM = alturaenCm / 100
imc = float(peso / (alturaenM * alturaenM))

def MostrarIMC(p_imc):
    resultado = ""
    if p_imc < imc_minimo:
        resultado = " ES DELGADO "
    if  p_imc > 20 and p_imc < 25:
        resultado = " ES NORMAL "
    if  p_imc >= imc_maximo:
        resultado = " ES GORDITO "
    return resultado

print ("su IMC es de :  " + str(imc))
print(MostrarIMC(imc))

"""
contador = 0
while contador <= 5:
    print ("El valor del contador es:  " + str(contador))
    contador += 1 

Seguir_chateando = True

while Seguir_chateando:

    emoji = input(">")
    if emoji == "salir":
        Seguir_chateando = False
    emoji = emoji.replace(":)", "😃")
    emoji = emoji.replace("UwU", "😍")
    emoji = emoji.replace(":p", "🤪")
    emoji = emoji.replace("B)", "😎")
    emoji = emoji.replace(":'(", "😢")
    emoji = emoji.replace("._.", "😐")
    emoji = emoji.replace("-_-", "😑")
    emoji = emoji.replace("-.-", "😡")
    emoji = emoji.replace("O.O", "😮")
    print(emoji)

arreglo = ["manzana", "banana", "pera", "melon"]
arreglo.reverse()
arreglo.remove("manzana")
arreglo.append("frutilla")
for frutas in arreglo:
    print("La fruta es: " + frutas)
    #recorrer textos
texto = "leandroid"
for letra in texto:
    print("Letra: " + letra)

for numero in range(10):
    if numero >= 0:
        print (numero)
           
"""