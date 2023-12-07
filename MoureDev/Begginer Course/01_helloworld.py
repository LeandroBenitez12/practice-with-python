# Printing "hello world"
print("Hola, Python")

# DYNAMIC TYPING
def print_variable(x):
    print(type(x))
    print(x)

my_string_full_name = "Leandro Benitez"

print_variable(my_string_full_name)

# my_string_full_name = 9
# print_variable(my_string_full_name)

my_int = 192
print_variable(my_int)

my_float = 177.923209

my_double = 11.11111134321232

result = my_int + my_float + my_double # sum of different variables
# result = my_int + my_float + my_string_full_name # error
print_variable(result)

my_bool = False

# transform data types 
print("hola soy leandro y tengo "+ str(my_int) + " y mido " + str(my_float))
print(f"hola soy leandro y tengo {my_int} y mido {my_bool}")

# lists
my_list = [my_string_full_name, my_int, my_bool, my_float, my_double] # podes agregar nuevos/remover valores, es ordenada
my_edad = 12
my_list.append(my_edad) # added new value to the list
print_variable(my_list)
print_variable(my_list[4])

# Dictionary 
my_dic = { "string" : my_string_full_name, "edad" : my_int, "bool" : my_bool, "peso": my_float,"c": my_double}

print_variable(my_dic)
print_variable(my_dic["edad"])

#set , permite no duplicar los valores y te entrega la info de forma desordenada
my_set = {my_string_full_name, my_int, my_bool, False,  my_float, my_double, my_double, "Gabriel", my_edad, my_string_full_name}
print_variable(my_set)

# tuple , una forma de almacenar valores que no puedan cambiar, esten ordenados y se puedan repetir
my_tuple ={my_string_full_name, my_int, my_bool, False,  my_float, my_double, my_double, "Gabriel", my_edad, my_string_full_name}

print("----------------------------------------------------------------")

def print_my_item(param):
    for my_item in param:
        print(my_item)
    return my_item

print_my_item(my_list)

print("----------------------------------------------------------------")

class DataType:
    def __init__(self, name, last_name, age, height_and_weight):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__height_and_weight = height_and_weight

    def printName(self):
        print(self.__name)
        
    def printlastName(self):
        print(self.__last_name)

    def printAge(self):
        print(self.__age)

    def printHnW(self):
        print(f'Su altura es: {self.__height_and_weight[0]} y su Peso: {self.__height_and_weight[1]}')
        
DataLeandro = DataType("Leandro", "Benitez", 19, [179, 80.6])
DataAgustin = DataType("Agustin", "Benitez", 59, [185, 89.6])

DataLeandro.printName()
DataLeandro.printHnW()

DataAgustin.printlastName()
DataAgustin.printAge()

inicio = 1
fin = 101

for i in range(inicio, fin):
    if(i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
    elif(i % 5  == 0):
        print("Buzz")
    elif(i % 3 == 0):
        print("Fizz")
    else:
        print(f" El numero es:  {i} ")
    
#Funciones
language = "HOLSA"
# primera letra mayuscula
print(language.capitalize())
# Todo en mayusculas
print(language.upper())
# contar letras o -
print(language.count(''))
#si es numero
print(language.isnumeric())
# minusculas
print(language.lower())

my_list2 = ['Leandro', 'Juana', 'Juan', 'Jose', 'Gabriel', 'Hernan']

print(my_list2)
elemento_eliminado = my_list2.pop()
print(my_list2)
print(f' el elemento eliminado es: {elemento_eliminado}')

# elimina por indice 
del my_list2[2]
print(my_list2)

# elimina por elemento 
my_list2.remove('Leandro')
print(my_list2)

#agregar el elemento al final
my_list2.append('Leandrito')
print(my_list2)

# insertar elemento donde quiera
my_list2.insert(0, '13')
print(my_list2)

#elementos de la lista
print(len(my_list2))