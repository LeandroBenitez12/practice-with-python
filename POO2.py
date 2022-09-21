class Car:
    def __init__(self, tipo, marca, mod, precio, patente, puertas, color):
        self.tipo = tipo
        self.marca =  marca
        self.modelo = mod
        self.precio = precio
        self.patente =  patente
        self.puertas = puertas
        self.color =  color
    
Car_c1 = Car('car Segment A','reno','clio', 1500000, 'ads0bc', 3 , 'gray')
Truck = Car('Truck','Mercedes Benz','Atego', 1500000, 'ao4lq2', 3 , 'brown')

print(Truck.marca)
print(Car_c1.modelo)
print(Truck.precio)