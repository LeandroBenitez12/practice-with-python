class Car:
    def __init__(self, tipo, marca, mod, precio, color):
        self._tipo = tipo
        self._marca =  marca
        self._modelo = mod
        self._precio = precio
        self._color =  color

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def marca(self):# metodo get
        print('llamando metodo get marca')
        return self._marca

    #@marca.setter #@(atribute_name.setter)
    #def marca(self, marca):
    #    print('llamando metodo set marca')
    #    self._marca = marca

    def mostrar_detalle(self):
        print(f'Car: {self._marca} {self._modelo} {self._precio}, {self._color}')

Car_c1 = Car('car Segment A','reno','clio', 1500000, 'gray')
Truck = Car('Truck','Mercedes Benz','Atego', 12345554300, 'brown')

Car_c1.marca = 'Mercedes'
print(Car_c1.marca)#recuperamos private get 


#Car_c1.mostrar_detalle()
#clase 96

Car_c1.Dueño = 'carlitos'
