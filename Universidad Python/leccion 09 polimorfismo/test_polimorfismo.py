from Employee import Employee
from Manager import Manager

def print_detail(object):
    #esto es un metodo generico,
    #podriamos preguntar si el metodo es de cierta instancia pero en python no es recomdable ya que no es bueno estar validando muchos datos
    print(type(object))
    print(object.show_detail())
    if isinstance(object, Manager):
    # preguntamos si el objeto que introducimos es manager entonces que imprima el atributo department
    #sino no imprime nada y no sale error si introducimos otro objeto, ej la clase  padre
        print(object._department)

Employee1 = Employee('David', 140000)
Manager1 = Manager('lEANDRO', 240000, 'BOLU2')

print_detail(Employee1)
print_detail(Manager1)
