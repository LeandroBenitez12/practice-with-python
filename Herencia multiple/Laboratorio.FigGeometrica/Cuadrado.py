from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color  ):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self , lado, lado)
        Color.__init__(self , color)
        
    def calcularArea(self):
        return self.height * self.width
    
    def __str__(self):
        return f'the square :  {FiguraGeometrica.__str__(self)}, and the {Color.__str__(self)}'
    