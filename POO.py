from re import A


class Motor:
    def __init__(self, ancho , alto):#constructora
        self.ancho = ancho
        self.alto = alto
    def calcularArea(self):
        area = self.ancho*self.alto
        return area
        
figura = Motor(10,12)  
print("el alto es: " + str(figura.alto))
print("el ancho es: " + str(figura.ancho))
print("el area es: " + str(figura.calcularArea()))
