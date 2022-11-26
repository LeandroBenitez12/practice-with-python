
from ast import If
from cgitb import text
from distutils.debug import DEBUG
from tkinter import Menu


def encriptar(texto):
    print("el texto a encriptar es: " + texto)
    textoFinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal


def desencriptar(texto):
    print("el texto a desencriptar es: " + texto)
    textoFinal = ""

    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)

    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoEncriptado)
    archivo.close()


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textodesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textodesencriptado)
    archivo.close()


contador = 0
while contador <= 3:
    menu = int(input("\n Select : 1(Encrypt) | 2(Decrypt) | 3(Encrypt the file) | 4(Decrypt the file):  "))


    if menu == 1:
        textoe = input(" the  a encriptar es: ")
        encriptar(textoe)
        print("Texo encriptado como: " + textoe)

    if menu == 2:
        textod = input(" El texto a desencriptar es: ")
        desencriptar(textod)
        print("Texo encriptado como: " + textod)

    if menu == 3:
        rutaArchivo = input("\n Enter the path of the file :  ")
        encriptarArchivo(rutaArchivo)
        print("the file has been succesfully encrypted. ")

    if menu == 4:
        rutaArchivo = input("\n Enter the path of the file :  ")
        desencriptarArchivo(rutaArchivo)
        print("the file has been succesfully decrypted. ")

    contador += 1
