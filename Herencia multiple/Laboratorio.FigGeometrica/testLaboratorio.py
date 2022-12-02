from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

Rectangle = Rectangulo(51, 5, 'Red')
Square = Cuadrado( 9, 'blue')
print(f'The calculate area is {Square.calcularArea()}')
print(Square)

print(f'The calculate area is {Rectangle.calcularArea()}')
print(Rectangle)