class Product:
    counter_products = 0

    @classmethod
    def generate_new_value (cls):
        cls.counter_products += 1
        return cls.counter_products

    def __init__(self, name , price):
        self._id_product = Product.generate_new_value()
        self._name = name
        self._price = price

    @property

    def name(self): #get = obtener
        return self._name 

    @name.setter #Set = modificar
    def name(self,name):
        self._name = name

    @property
   
    def price(self): #get = obtener
        return self._price

    @price.setter #Set = modificar
    def price(self,price):
        self._price = price

    def __str__(self):
        return f'ID Product : {self._id_product}, Name: {self._name}, Price: {self._price} '

if __name__ == '__main__':
    product1 = Product('jeans', 3000)
    product2 = Product('shirt', 4000)
    print(product1)
    print(product2)

