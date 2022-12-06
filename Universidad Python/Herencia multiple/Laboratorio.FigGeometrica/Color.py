class Color:
    def __init__(self, color):
        self._color = color

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def color(self):
        return self._color
    
    @color.setter #metodo de tipo set asociado a ese atributo
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'The color is:  {self._color}'