from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo (FiguraGeometrica, Color ):
    def __init__(self, height, width, color):
        FiguraGeometrica.__init__(self , height, width)
        Color.__init__(self , color)
    
    def calculate_Area(self):# AGREMAMOS IMPLEMENTACION DEL METODO ABSTRACT
        return self._height * self._width
    
    def __str__(self):
        return f'the rectangle have a height of : {self._height}, a width of :  {self._width}, and Color is : {self._color}'
    