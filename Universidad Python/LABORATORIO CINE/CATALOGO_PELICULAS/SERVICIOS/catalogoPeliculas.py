from Add_recursos import Add_recursos
import os 
class CatalogoPeliculas:
    rutaArchive = 'D:\\GIT\\Course Phyton\\Universidad Python\\LABORATORIO CINE\\CATALOGO_PELICULAS\\CATALOGO_PELICULAS.txt'
    
    @classmethod
    def addMovie(cls, pelicula):
        with Add_recursos(cls.rutaArchive , 'a') as archivo:
            archivo.write(f'{pelicula.name}\n')
            print('adding succesfully')
    @classmethod
    def listarPelis(cls):
        with open(cls.rutaArchive, 'r' , encoding='utf8') as archivo:
            print('Catalogo Peliculas'.center(50 , '-'))
            print(archivo.read())
    @classmethod
    def eliminate(cls):
        os.remove(cls.rutaArchive)
        print('Archivo eliminado es: {cls.rutaArchive}')