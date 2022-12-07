from Product import *

class Order:
    counter_order = 0

    @classmethod
    def generate_new_value(cls):
        cls.counter_order = cls.counter_order + 1
        return cls.counter_order

    def __init__(self, products):
        self._id_order = Order.generate_new_value()
        self._products = list(products)#la convertimos a una lista y si no es una lista realmente manda error

    def add_product(self, product):
        self._products.append(product)

    def calculate_total(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def __str__(self):
        product_str = ''
        for product in  self._products:
            product_str += product.__str__() + '|'


        return f'Order: {self._id_order} \nproducts: {product_str}'

if __name__ == '__main__':
    product1 = Product('jeans', 3000)
    product2 = Product('shirt', 4000)
    product3 = Product('Cap', 2000)
    product4 = Product('T-shirt', 2300)
    product5 = Product('short', 1800)
    product6 = Product('stockings', 500)
    product7 = Product('boxer', 1000)
    
    products1 = [product1, product2, product3]
    products2 = [product4, product5, product6]
    products3 = [product7, product5, product4]

    Orden1 = Order(products1)
    Orden2 = Order(products2)
    Orden3 = Order(products3)
    
    print(Orden1)
    print(Orden2)
    print(Orden3)
else:
    print (__name__)