# Exception Handling ( Manejo de errores )

try:
    number_one = int(input("Ingrese un numero: "))
    numbre_two = int(input("Ingrese un segundo numero: "))
    print(f" La suma del numero {number_one} + {numbre_two} es igual a {number_one + numbre_two} ")
    print("No ocurrio error")
except:
    print("Ha ocurrido un error") # si ocurre Exception imprime
else: # Opcional
    print("El programa sigue bien") # se ejecuta si no ocurrio Exceptions
finally: # Opcional
    print("el programa continua") # se ejecuta siempre 


# Tipos de Exceptions

try:
    print(f'la suma es: {5 +'count'}')
except TypeError:
    print('Error de tipeado PAA')
except ValueError:
    print('Error de valor PAAa')
finally:
    print('Seguimo')

