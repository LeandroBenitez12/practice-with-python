from Employee import Employee
from Manager import Manager

def print_detail(object):
    
    print(type(object))
    print(object.show_detail())

Employee1 = Employee('David', 140000)
Manager1 = Manager('lEANDRO', 240000, 'BOLU2')

#print_detail(Employee1)
print_detail(Manager1)
