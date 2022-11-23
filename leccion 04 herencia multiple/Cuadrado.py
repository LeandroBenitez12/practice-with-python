from Color import *
from FiguraGeometrica import *

class Cuadrado ( FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__()
        FiguraGeometrica.__init__(self , lado, lado)
        Color.__init__(self , color)
    def calcularArea(self):
        return self.alto * self.ancho