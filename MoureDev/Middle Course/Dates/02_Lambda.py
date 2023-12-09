### Lambda ###
# Que es ? Lambda es una funcion pequeña y anonima, sirve para reducir codigo
# Ejemplo con queres hacer un lambda de 2 entradas , para que se sumen entre si

sum_two_values = lambda n_one, n_two : n_one + n_two

print(type(sum_two_values(3,9)))

fahrenheit_degrees = lambda celsius_degrees : print(f'The {celsius_degrees} ºC degrees are equal {celsius_degrees * 9/5 + 32} ºF degrees')

fahrenheit_degrees(24)