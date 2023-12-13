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

csv_file =open(path_csv, 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Surname', 'Age', 'Nationality' , 'id'])
csv_writer.writerow(['Leandro', 'Benitez', 19 , 'Argentina' , 11060])
csv_writer.writerow(['Juan', 'Benitez', 17 , 'Argentina' , 1964560])
csv_writer.writerow(['Gabriel', 'Benitez', 26 , 'Argentina' , 145623])


csv_file.close()

with open (path_csv, 'r+') as my_other_file_cvs:
    for line in my_other_file_cvs.readlines():
        print(line)


# .xml file
import xml.etree.ElementTree as ET

path_xml = 'MoureDev/Middle Course/Dates/file.xml'

try: 
    xml_file = open(path_xml) # 'W+' ES PARA CREAR ARCHIVO SI NO LO ESTA Y ESCRIBE 
    # print(xml_file.read()) # datos sin formato
    if xml_file.readable():
        print(True)
        xml_data = ET.fromstring(xml_file.read())
        print(xml_data)
        date_list = xml_data.findall(path_xml)
        for elemento in date_list:
            print(f'Libro: {elemento.find('titulo').text}')
            print(f'Autor: {elemento.find('autor').text}')
            print('------')
    else:   
        print(False)
except Exception as e :
    print(f'Error: {e}')
finally:
    xml_file.close()

