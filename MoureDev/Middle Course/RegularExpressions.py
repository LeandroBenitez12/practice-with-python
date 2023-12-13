### RegulaR Expressions ###

"""
Las expresiones regulares en Python (también conocidas como regex) 
son secuencias de caracteres que forman un patrón de búsqueda.
Se utilizan para buscar y manipular cadenas de texto, 
permitiendo realizar operaciones sofisticadas de búsqueda,
extracción, reemplazo o validación de patrones dentro de cadenas.
"""

import re

my_string_password = '#DIOSITOestaC0nm1g0*.'
my_other_password = '#DIOSITOesta4qui*.*.'
print(re.match("esta", my_string_password)) #match empieza a buscar desde el principio

