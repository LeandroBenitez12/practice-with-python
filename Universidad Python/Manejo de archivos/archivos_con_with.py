from Manager_recursos import Manager_recursos

with Manager_recursos('D:\\GIT\\Course Phyton\\Universidad Python\\Manejo de archivos\\prueba.txt') as archivo:
      print(archivo.read())