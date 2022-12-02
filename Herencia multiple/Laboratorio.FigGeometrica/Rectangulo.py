from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo (FiguraGeometrica, Color ):
    def __init__(self, h, base, color):
        FiguraGeometrica.__init__(self , h, base)
        Color.__init__(self , color)
    
    def calcularArea(self):
        return self._height * self._width
    
    def __str__(self):
        return f'the rectangle have a height of : {self._height}, a width of :  {self._width}, and Color is : {self._color}'
    