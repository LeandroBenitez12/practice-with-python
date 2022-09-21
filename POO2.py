class Automovil:
    def __init__(self, marca, mod, precio, patente, puertas, color):
        self.marca =  marca
        self.modelo = mod
        self.precio = precio
        self.patente =  patente
        self.puertas = puertas
        self.color =  color
    
Camion = Automovil('reno','clio', 1500000, 'ads0bc', 3 , 'gris')
print(Camion.marca)
print(Camion.modelo)
print(Camion.precio)