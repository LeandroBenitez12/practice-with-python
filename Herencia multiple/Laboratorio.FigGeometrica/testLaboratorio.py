from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#no se puede intanciar una class abstract
#Figura = FiguraGeometrica(4, 8)
LADOS = 4

print('Creation Object Square'.center(50, '-'))#rellenamos con guiones medios
Square = Cuadrado( lado=8, color= 'blue')#autodocumentamos codigo
Square.width = LADOS#vALIDACIONES
Square.height = LADOS
print(f'The calculate area is {Square.calculate_Area()}')
print(Square)

print('')
print('Creation Object Rectangle'.center(50, '-'))#rellenamos con guiones medios
Rectangle = Rectangulo(height= 4, width= 2,  color= 'Red')#autodocumentamos codigo
Rectangle.height = 14
print(f'The calculate area is {Rectangle.calculate_Area()}')
print(Rectangle)