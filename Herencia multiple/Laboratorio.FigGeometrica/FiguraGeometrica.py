class FiguraGeometrica:
    def __init__(self, width , height):
        #validate if the variable width or height is less than 50
        if 0 <= width < 50:
            self._width = width
        else:
            self.width = 0
        
        if 0 <= height < 50:
            self._height = height
        else:
            self.height = 0

    def __str__(self):
        return f'the geometric figure have a height of : {self._height}, and a width of :  {self._width}'
    
    #set = modificar| get = obtener
    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def width(self):
        return self._width
    
    @width.setter #metodo de tipo set asociado a ese atributo
    def width(self, width):
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter #metodo de tipo set asociado a ese atributo
    def height(self, height):
        self._height = height
