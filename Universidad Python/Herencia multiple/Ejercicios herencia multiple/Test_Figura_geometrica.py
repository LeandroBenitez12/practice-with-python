from Cuadrado import Cuadrado

numero = int(input(" ingresa LA ALTURA Y ANCHO DE LOS LADOS DL PUTO CUADRAD0 el n la reputa que te pario:  "))
color = str(input(" el color del CUADRAD0 (IMBECIL)ahora ingresa corneta:  "))
SquareGreen = Cuadrado( numero, color)

print((f' el ancho del square :  {SquareGreen.ancho}' ))
print((f' el alto del square :  {SquareGreen.alto}' ))
print((f' el color del square :  {SquareGreen.color}' ))
print(f'the calculo del area del square: {SquareGreen.calcularArea()} ')

#MRO = method resolution order 
MRO = Cuadrado.mro()   
print(MRO)
