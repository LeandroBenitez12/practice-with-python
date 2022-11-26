class Cubo:
    def __init__(self, ancho, alto, profundo):
        self._ancho = ancho
        self._alto = alto
        self._profundo = profundo   

    def CalcularVolume(self):
        return self.ancho* self.alto * self.profundo

Ancho = int(input ("Ingrese el ancho del Cubo: "))
Alto = int(input ("Ingrese la altura del Cubo: "))
Profundidad = int(input ("Ingrese la profundidad del Cubo: "))

Cubo_1 = Cubo(Ancho, Alto, Profundidad)

print (f"el volumen del cubo es: {Cubo_1.CalcularVolume()}")