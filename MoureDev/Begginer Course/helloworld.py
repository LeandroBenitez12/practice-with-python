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

my_bool = True

# transform data types 
print("hola soy leandro y tengo "+ str(my_int) + " y mido " + str(my_float))
print(f"hola soy leandro y tengo {my_int} y mido {my_bool}")

# lists
my_list = [my_string_full_name, my_int, my_bool, my_float, my_double]
my_edad = 12
my_list.append(my_edad)
print_variable(my_list)
print_variable(my_list[4])

# Dictionary 
my_dic = { "string" : my_string_full_name, "edad" : my_int, "bool" : my_bool, "peso": my_float,"c": my_double}

print_variable(my_dic)
print_variable(my_dic["edad"])