from Pelicula import Pelicula
from Add_recursos import Add_recursos
import os 
class CatalogoPeliculas(Pelicula):
    rutaArchive = 'Peliculas.txt'
    def __init__(self, Pelicula):
        super().__init__(Pelicula)
        Pelicula.__init__(Pelicula)
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