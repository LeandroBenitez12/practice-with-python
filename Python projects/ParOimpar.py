def parOimpar(num):
    Value= num % 2
    if bool(Value) == 0:
        print(f' el numero {num} es par')
    else:
        print(f' el numero {num} es impar')

numero = int(input(' Ingrese un numero para saber si es par o impar:   '))

parOimpar(numero)
