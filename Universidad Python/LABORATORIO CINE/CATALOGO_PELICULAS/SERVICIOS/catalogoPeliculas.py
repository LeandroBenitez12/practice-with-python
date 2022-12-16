from Pelicula import Pelicula

class CatalogoPeliculas(Pelicula):
    rutaArchive = None
    def __init__(self, Pelicula):
        super().__init__(Pelicula)
        Pelicula.__init__(Pelicula)
    @classmethod
    def add(cls,pelicula):
        