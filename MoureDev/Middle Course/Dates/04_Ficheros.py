### File handling ###

# Manejo de archivos
import os

# Debugs
delete_file_txt = False
update = False

#paths
txt_path ='MoureDev/Middle Course/Dates/file.txt'


# .txt file 

with open(txt_path, "r+") as txt_file: # read and write
    # txt_file.write("leandro benitez\n18 años\nDNI\n46023790\n13/07/2004\nMonte grande") 
    info = []
    for i in txt_file.readlines(): 
        info.append(i.strip()) # strip() es una funcion para eliminar caracteres vacios de cada linea
    print(info)

if update:
    with open(txt_path, "a") as my_other_file:
        #my_other_file.write("\nBuenos Aires") # escribo
        my_other_file.write("\n Tecnico Electronico")

if delete_file_txt:
    txt_file.close()
    os.remove(txt_path)

# .json file

json_path = 'MoureDev/Middle Course/Dates/file.json'
delete_file_json = False

import json

json_file = open(json_path, 'r+') # crear archivo json

json_test = { "name" : 'leandro',
              'surname' : ['benitez', 'fernandez', 'canete'], 
              "edad" : 19 , 
              "lives?" : True , 
              "peso": 81 ,
              "state": 'soltero'}

json_test_2 = { "name" : 'juan',
              'surname' : ['benitez', 'fernandez', 'canete'], 
              "edad" : 17 , 
              "lives?" : True , 
              "peso": 76 ,
              "state": 'soltero'}
# json_file.write(json_test) # error

json.dump(json_test, json_file, indent=2) # escribir fichero json

json_file.close()

with open(json_path) as my_other_file_json:
    # json.dump(json_test_2, my_other_file_json, indent= 2 )
    for i in my_other_file_json.readlines():
        print (i)


if delete_file_txt:
    json_file.close()
    os.remove(json_path)

json_dict = json.load(open(json_path))

print(json_dict)

# .csv file 

import csv

path_csv =  'MoureDev/Middle Course/Dates/file.csv'

csv_file =  open(path_csv, 'w+')

csv_writer = csv.writer 



# .xls file

