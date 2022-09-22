class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
#erro en self del metodo area
    def Area(self):
        return self.altura * self.base

altura = int(input('ingrese un numero para la altura del rectangulo: '))
base = int(input('ingrese un numero para la base del rectangulo: '))

rec1 = Rectangulo(altura, base)

print(rec1.Area())    