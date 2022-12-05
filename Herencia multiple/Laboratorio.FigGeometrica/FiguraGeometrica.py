#ABC abstract base class
from abc import ABC, abstractmethod #separamos con coma para importar mas de un elemento
class FiguraGeometrica(ABC):
    def __init__(self, width , height):
        #validate if the variable width or height is less than 50
        if self._validate_value(width):
            self._width = width
        else:
            self.width = 0
            print(f'value error width : {width}')
        
        if self._validate_value(height):
            self._height = height
        else:
            self.height = 0
            print(f'value error height : {height}')


    #set = modificar| get = obtener
    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def width(self):
        return self._width
    
    #si deseamos que solo sea de lectura podemos comentar/eliminar el setter    
    @width.setter #metodo de tipo set asociado a ese atributo
    def width(self, width):
        if self._validate_value(width):#propagamos errores a los setter
            self._width = width
        else:
            print(f'value error width : {width}')
    
    @property
    def height(self):
        return self._height
    
    #si deseamos que solo sea de lectura podemos comentar/eliminar el setter
    @height.setter #metodo de tipo set asociado a ese atributo
    def height(self, height):
        if self._validate_value(height):#propagamos errores a los setter
            self._height = height
        else:
            print(f'value error height : {height}')

    @abstractmethod
    def calculate_Area(self):
        pass

    def __str__(self):
        return f'the geometric figure have a height of : {self._height}, and a width of :  {self._width}'
    
    def _validate_value(self, value):#initialize width a '-' to indicate method private
        return True if 0 < value < 10 else False # Retornamos validacion sintaxis simplificada if else