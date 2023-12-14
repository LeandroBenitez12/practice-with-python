### RegulaR Expressions ###

"""
Las expresiones regulares en Python (también conocidas como regex) 
son secuencias de caracteres que forman un patrón de búsqueda.
Se utilizan para buscar y manipular cadenas de texto, 
permitiendo realizar operaciones sofisticadas de búsqueda,
extracción, reemplazo o validación de patrones dentro de cadenas.
"""

import re

my_string = 'Hello my name is Leandro'
my_other_string = 'Dios esta aqui'
print(re.match('DIOS esta', my_other_string, re.I)) #match empieza a buscar desde el principio
print(re.match(" ios esta", my_other_string))

find_one = re.match('DIOS esta ', my_other_string, re.I)
print(find_one.span())
