class Car:
    def __init__(self, tipo, marca, mod, precio, color):
        self.tipo = tipo
        self.marca =  marca
        self.modelo = mod
        self.precio = precio
        self.color =  color
    
    def mostrar_detalle(self):
        print(f'Car: {self.marca} {self.modelo} {self.precio}, {self.color}')

Car_c1 = Car('car Segment A','reno','clio', 1500000, 'gray')
Truck = Car('Truck','Mercedes Benz','Atego', 12345554300, 'brown')

Car_c1.mostrar_detalle()

Truck.km = 40032

print(Truck.km)
