# this is the coment
from typing import TextIO


print("Hello Word , I'm Leandro Benitez")
"""
COMENT 
"""
# variables
TEXTO = "riBer te fuiste"
DONDE = "a la B"
PORQUE = "por puto y cagon en: "
YEAR = 2011
# string variables
print(f"{TEXTO} {DONDE} {PORQUE} {str(YEAR)} ")
"""
# input of the data
sitioweb = input ("what is your website?")
print("the website is : " + sitioweb)
"""
# condicionals
var_edad = int(input("how old are you?"))
def MostrarEdad(edad):
    Result = ""
    edad_minima = 18
    if edad >= (edad_minima):
        Result = "You are of legal age, you can access!"
    else:
        Result = "Access denied for minors"
    return Result

print(MostrarEdad(var_edad))
 
#list
persons = ["Leandro", "Juan", "Gabriel"]
#print(persons[0])

for person in persons:
    print("-" + person)

    


