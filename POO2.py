class Car:
    def __init__(self, tipo, marca, mod, precio, color):
        self.__tipo = tipo
        self.__marca =  marca
        self.__modelo = mod
        self.__precio = precio
        self.__color =  color
    
    def mostrar_detalle(self):
        print(f'Car: {self.__marca} {self.__modelo} {self.__precio}, {self.__color}')

Car_c1 = Car('car Segment A','reno','clio', 1500000, 'gray')
Truck = Car('Truck','Mercedes Benz','Atego', 12345554300, 'brown')
Car_c1.__marca = 40032
Car_c1.mostrar_detalle()
#clase 96

Car_c1.Dueño = 'carlitos'
