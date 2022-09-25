class Car:
    def __init__(self, tipo, marca, mod, precio, color):
        self._tipo = tipo
        self._marca =  marca
        self._modelo = mod
        self._precio = precio
        self._color =  color

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def marca(self):# metodo get
        #print('llamando metodo get marca')
        return self._marca

    #@marca.setter #@(atribute_name.setter)
    #def marca(self, marca):
    #    print('llamando metodo set marca')
    #    self._marca = marca

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def modelo(self):# metodo get
        #print('llamando metodo get modelo')
        return self._modelo

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def precio(self):# metodo get
        #print('llamando metodo get precio')
        return self._precio

    @property #decorador , modifica el metodo para solo acceder al atributo atravez del metodo, tipo te hace ahorrar los '()'
    def color(self):# metodo get
        #print('llamando metodo get color')
        return self._color

    def mostrar_detalle(self):
        print(f'Car: {self._marca} {self._modelo} {self._precio}, {self._color}')

Car_c1 = Car('car Segment A','reno','clio', 1500000, 'gray')
Truck = Car('Truck','Mercedes Benz','Atego', 12345554300, 'brown')

#Car_c1.marca = 'Mercedes'
#Car_c1.modelo = 'm1b'
#Car_c1.precio = 12121314
#Car_c1.color = 'yelou'



#Car_c1.mostrar_detalle()
#clase 96

Car_c1.Dueño = 'carlitos'
if __name__ == '__main__':
    print(__name__)
    Truck.mostrar_detalle()
    print(Car_c1.precio)#recuperamos private get 

