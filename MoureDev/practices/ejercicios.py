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
    if n1 > n2 > n3:
        return n1
    elif n1 < n2 > n3:
        return n2
    elif n1 < n2 < n3:
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
        
input_str = str(input("Ingrese una letra: "))
print(esVocal(input_str))