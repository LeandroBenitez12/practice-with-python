
class Order:
    counter_order = 0

    @classmethod
    def generate_new_value(cls):
        cls.counter_order += 1
        return cls.counter_order

    def __init__(self, Computers):
        self._id_order = Order.generate_new_value()
        self._Computers = list(Computers)#la convertimos a una lista y si no es una lista realmente manda error

    def add_Computer(self, Computer):
        self._Computers.append(Computer)

    def __str__(self):
        Computers_str = ''
        for Computer in  self._Computers:
            Computers_str += Computer.__str__() + ''
        
        return f'''
        Order: {self._id_order} 
        Computers: {Computers_str}
        
        '''