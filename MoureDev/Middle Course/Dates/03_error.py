### Error Types ###
# repaso todas las excepciones de python

# SytaxError

# print "hola comunidad" #error
print("hola comunidad")

nombre = 'Gusti'
# NameError
# print(name) #error
print(nombre)

# IndexError
my_list = ['name', "2", "3", "4"]
# print(my_list[4]) #  error: el indice de la lista esta fuera de rango
print(my_list[3])

# ModuleNotFoundError

# import maths # Error
import math

# AtTributeError 
#print(math.PI) # error
print(math.pi)

# kEYeRROR
my_dict = {'name' : 'lean', 'years': '19', 'state' : 'single'}
# print(my_dict[0]) # error
# print(my_dict['nombre']) # error
print(my_dict['name'])

# TypeError
# print('a'+ 2) # error
#print(my_list['name']) #error
print(my_list[0])

#valueError
# lo pasamos de manera correcta a int
my_int = int('100')
#my_int = int('tengo 10')# Error
print(type(my_int))

# Zerodivisionerror( especifico cuando hacemos divisiones entre 0)

# estos serian los errores que tiene incorporado python por defecto