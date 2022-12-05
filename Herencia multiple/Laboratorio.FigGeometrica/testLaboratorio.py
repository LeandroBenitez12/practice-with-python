from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

LADOS = 4

print('Creation Object Square'.center(50, '-'))#rellenamos con guiones medios
Square = Cuadrado( lado=8, color= 'blue')#autodocumentamos codigo
Square.width = LADOS
Square.height = LADOS
print(f'The calculate area is {Square.calcularArea()}')
print(Square)

print('')
print('Creation Object Rectangle'.center(50, '-'))#rellenamos con guiones medios
Rectangle = Rectangulo(height= 4, width= 2,  color= 'Red')#autodocumentamos codigo
Rectangle.height = 14
print(f'The calculate area is {Rectangle.calcularArea()}')
print(Rectangle)