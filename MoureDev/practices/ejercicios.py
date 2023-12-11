"""Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def maxFunction(n1: int , n2: int):
    

    if n1 > n2 :
        return n1
    elif( n1 < n2):
        return n2
    elif (n1 == n2):
        raise Exception("Los valores no pueden ser iguales")
    else:
        raise Exception("Algo salio Mal")
    
print(maxFunction(0,7))

def maxThree(n1: int, n2: int, n3: int):
    if n1 > n2 and n1 > n3:
        return n1
    elif n1 < n2 and n2 > n3:
        return n2
    elif n1 < n3 and n2 < n3:
        return n3
    elif n1 == n2 == n3:
        raise Exception("los valores no pueden ser iguales")
    else:
        raise Exception("Algo salio mal")
    
print(maxThree(-15, 1 ,3))

def esVocal(letra: str):
    Vocal = ['a', 'e', 'i','o','u']
    letra = letra.lower()
    for i in Vocal:
        if letra == i:
            return True
    
    return False
        
# input_str = str(input("Ingrese una letra: "))
# print(esVocal(input_str))

def generador_caracteres(n: int, letra: str):
    return letra * n

print(generador_caracteres(5,'s'))

def sum_list(lista: list):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")
    result = 0
    for lista in lista:
        result = lista + result     
    return result

print(sum_list([6,0,4,-3]))

def mult_list(lista: list):
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")
    result = 1
    for i in lista:
        result = i*result
    return result

print(mult_list([1,2,-4,-3]))

def dereversaMami(text: str):
    text = list(text)
    inverso = ''
    for caracter in range(0, len(text)):
        inverso += text[len(text) - caracter - 1]
    return inverso

print(dereversaMami("Leandro"))

def es_palindromo(text):
    text_inverso = dereversaMami(text)
    if text == text_inverso:
        return True
    else:
        return False

# print(es_palindromo('RADAR'))

def superposicion(lista1, lista2):
    """for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True"""
    for elemento1 in lista1:
        if elemento1 in lista2:
            return True
    
    
print(f'Superposicion:  {superposicion([1,2,3], [0,6,0])}')

def histograma(lista):
    for n in lista:
        print(n * '*')
    
        
print(histograma([4,3,2,1,0]))

def grafico(n):
    n = -n
    for i in range(n, 1):
        i = abs(i)
        print('*' * i)

grafico(10)