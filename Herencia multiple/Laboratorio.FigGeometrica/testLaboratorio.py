from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creation Object Square'.center(50, '-'))#rellenamos con guiones medios
Square = Cuadrado( lado=9, color= 'blue')#autodocumentamos codigo
print(f'The calculate area is {Square.calcularArea()}')
print(Square)

print('Creation Object Rectangle'.center(50, '-'))#rellenamos con guiones medios
Rectangle = Rectangulo(height= 51, width= 25,  color= 'Red')#autodocumentamos codigo
print(f'The calculate area is {Rectangle.calcularArea()}')
print(Rectangle)