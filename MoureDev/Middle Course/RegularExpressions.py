### RegulaR Expressions ###

"""
Las expresiones regulares en Python (también conocidas como regex) 
son secuencias de caracteres que forman un patrón de búsqueda.
Se utilizan para buscar y manipular cadenas de texto, 
permitiendo realizar operaciones sofisticadas de búsqueda,
extracción, reemplazo o validación de patrones dentro de cadenas.
Esta fuera de python , todos los lenguajes aceptan Regex
"""

import re

my_string = 'Hello my name is Leandro, they tell me leo, but i do not like it , i like being called lean o LEAN, i am 19 years'
my_other_string = 'Dios esta aqui'
print(re.match('Dios Esta ', my_other_string, re.I)) #match empieza a buscar desde el principio
print(re.match(" ios esta", my_other_string))

# find_one = re.match('DIOS esta ', my_other_string, re.I)
find_one = re.match('DIOS esta ', my_string, re.I)
# if not(find_one == None):
# if find_one != None:
if find_one is not None:
    span = find_one.span()
    print(type(span))
    start, end = span
    print(f'Se nos muestra: "{my_other_string[start:end]}"')
else:
    print('Termino')

# search
search = re.search('lean', my_string, re.I) # search encuentra por cualquier lugar el str
print(search)
print(search.span())
s, e = search.span()
print(f'el termino encontrado es : "{my_string[s:e]}"')

# findall

findall = re.findall('LEan', my_string, re.I) # nos devuelve una lista con las veces que encuentra el str en el texto
print(findall)

#split 
print(re.split(",", my_string)) # es un patron , el cual separa segun el pattern que le demos y lo divide en diferentes elementos de una lista

# sub 
my_string = re.sub('Hello my name is', 'Hola mi nombre es', my_string)
print(my_string) # substituye str, NO LLEVA ,re.I
print(re.sub('leo|LEO|Leo', 'LeitodeMG', my_string)) #poner para que encuentre varias str y en caso de encontrar substituir
print(re.sub('[L|l]eo|LEO', 'LeitodeMG', my_string)) #manera simplificada y patron


# Patterns
pattern = r'[Ll]ean|LEAN' #patron para dos o tres opciones

print(re.findall(pattern, my_string))
pattern = r'[0-9]' # patron para numeros de 0 a 9
print(re.findall(pattern, my_string)) 

"""
\d: Coincide con cualquier dígito decimal (0-9).
\D: Coincide con cualquier carácter que no sea un dígito.
\w: Coincide con cualquier carácter alfanumérico (letras, números y guiones bajos).
\W: Coincide con cualquier carácter que no sea alfanumérico.
\s: Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, saltos de línea).
\S: Coincide con cualquier carácter que no sea un espacio en blanco.
.: Coincide con cualquier carácter, excepto un carácter de nueva línea.
"""

pattern = r'\W' # PATRON DE BUSQUEDA DE LETRA / NUMERO, ETC
print(re.findall(pattern, my_string))

pattern = r'[lL].*' # PATRON DE BUSQUEDA DE LETRA, * desde primer letra completa todo hasta la ultima
print(re.findall(pattern, my_string)) # encuentra coincidencias con esta letra

# Utilizamos Regex para validacion de numeros y emails ,etc

# email validation Regular Expression

#patterns
#la r al inicio de patron significa que lo que sigue es un regex

email = 'lean-svae9@gmail.es'
pattern = r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$" # \. es para poner el .  $: Coincide con el final de la cadena.
print(re.findall(pattern, email))
print(re.search(pattern, email))
search = re.search(pattern, email)
if search is not None:
    start, end = search.span()
    print(email[start:end])

    # para aprender y validar REGEX -> https://regex101.com