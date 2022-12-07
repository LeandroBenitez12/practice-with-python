from Order import Order
from Product import *

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
print(f'Total Order: $ {Orden1.calculate_total()}')
print(Orden2)
print(f'Total Order: $ {Orden2.calculate_total()}')
print(Orden3)
print(f'Total Order: $ {Orden3.calculate_total()}')
