class Pelicula:
    def __init__(self,pelicula):
        self.__pelicula = pelicula

    def __str__(self):
        return f' the movie is: {self.__pelicula}'