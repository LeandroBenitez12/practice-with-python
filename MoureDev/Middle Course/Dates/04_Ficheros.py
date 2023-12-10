### File handling ###
# Manejo de archivos
import os
# .txt file
delete_file = False
txt_file = open("MoureDev/Middle Course/Dates/file.txt", "r+") # read and write

# txt_file.write("leandro benitez\n18 años\nDNI\n46023790\n13/07/2004\nMonte grande")

#print(txt_file.readline())
#print(txt_file.readline())

info = []
for i in txt_file.readlines(): 
    info.append(i.strip()) # strip() es una funcion para eliminar caracteres vacios de cada linea

print(info)



# with open("MoureDev/Middle Course/Dates/file.txt", "a") as my_other_file:
#     my_other_file.write("\nBuenos Aires") # escribo
#     my_other_file.write("\n Tecnico Electronico")
if delete_file:
    txt_file.close()
    os.remove('MoureDev/Middle Course/Dates/file.txt')

import json

json_file = open('MoureDev/Middle Course/Dates/file.json', 'w+') # crear archivo json

json_test = { "name" : 'leandro',
              'surname' : ['benitez', 'benitez', 'cañete'], 
              "edad" : 19 , 
              "lives?" : True , 
              "peso": 80.7 ,
              "state": 'soltero'}

# json_file.write(json_test) # error

json.dump(json_test, json_file, indent=2) # escribir fichero json