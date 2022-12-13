archivo = open('D:\\GIT\\Course Phyton\\Universidad Python\\Manejo de archivos\\prueba.txt', 'r', encoding= 'utf8')#no es necesary especificar las rutas pero si estamos en windows
#print(archivo.read())#comentar esta linea para leer alguno caracteres

#leer algunos caracteres
#print(archivo.readline())
#print(archivo.readline())

# iterar el archivo
#for linea in archivo:
#    print(linea)

# leer lines
#print(archivo.readlines())

#aceder a una linea de la lista 
#print(archivo.readlines()[2])

#abrir new file 
#anexamos a informacion
archivo2 = open('D:\\GIT\\Course Phyton\\Universidad Python\\Manejo de archivos\\copia.txt', 'w', encoding= 'utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se termino the process de leer y copiar archivos')
