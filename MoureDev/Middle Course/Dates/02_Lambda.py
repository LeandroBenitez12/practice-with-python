### Lambda ###
# Que es ? Lambda es una funcion pequeña y anonima, sirve para reducir codigo
# Ejemplo con queres hacer un lambda de 2 entradas , para que se sumen entre si

sum_two_values = lambda n_one, n_two : n_one + n_two

print(type(sum_two_values(3,9)))

fahrenheit_degrees = lambda celsius_degrees : print(f'The {celsius_degrees} ºC degrees are equal {celsius_degrees * 9/5 + 32} ºF degrees')

fahrenheit_degrees(24)

### Higher order functions ###
# Funcion de orden superior , funciones dentro de funciones

def suma(num):
    def resta(n2):
        return num + num - n2
    return resta

sum = suma(3)

print(sum(2))

def suma(num):
    def resta(n2):
        return num + num - n2
    return resta

print((suma(2))(1))

# MAP funcion donde debes poner una funcion y un elemento iterable , lo que hace es ejecutar la funcion proporcionada en cada elemento de la iteracion

def multiplication(num):
    return num * num

my_list = [3, 5, 2, 34, 10, 100, -10000, 6, 3 , 34, 5]
print(tuple(map(lambda n1 : n1 * n1, my_list)))
print(list(map(multiplication, my_list)))
# filter , capaz de elegir un criterio, requiere una funcion boleana( de criterio) y una lista iterable, es un filtrado

def thereIsObject(num):
    if num >= 60:
        return True
    else: False

print(list(filter(thereIsObject, my_list)))
print(list(filter(lambda num : num >= 60 , my_list)))

from functools import reduce 
# Reduce , necesitas una funcion lambda con 2 argumentos 
# , lo que hace es iterar esos dos argumentos del primero al ultimo de la lista,
# se puede concatenar cadenas de texto, sumar numeros o multiplicarlos en cadena, 
# encontrar el numero mayor de una lista
#  

print(reduce(sum_two_values, my_list))

print(reduce(lambda x, y: y if y < x else x , my_list))