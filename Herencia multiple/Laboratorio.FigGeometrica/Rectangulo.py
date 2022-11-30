from Color import *
from FiguraGeometrica import *

class Rectangulo (Color , FiguraGeometrica):
    def __init__(self, h, base, color):
        #super().__init__()
        FiguraGeometrica.__init__(self , h, base)
        Color.__init__(self , color)
    def calcularArea(self):
        return self.alto * self.ancho