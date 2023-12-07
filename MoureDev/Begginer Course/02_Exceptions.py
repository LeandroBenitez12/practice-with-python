# Exception Handling ( Manejo de errores )

try:
    number_one = int(input("Ingrese un numero: "))
    numbre_two = int(input("Ingrese un segundo numero: "))
    print(f" La suma del numero {number_one} + {numbre_two} es igual a {number_one + numbre_two} ")
    print("No ocurrio error")
except:
    print("Ha ocurrido un error")
