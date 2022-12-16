class Pelicula:
    def __init__(self,pelicula):
        self.__pelicula = pelicula

    def __str__(self):
        return f' the movie is: {self.__pelicula}'
    
    @property
    def name(self):
        return self.__pelicula

    @name.setter
    def name(self, name):
        self.__pelicula = name 
        