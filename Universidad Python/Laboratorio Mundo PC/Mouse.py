from inputDevice import inputDevice
class Mouse(inputDevice):
    mouse_counter = 0

    @classmethod
    def generate_new_value (cls):
        cls.mouse_counter += 1
        return cls.mouse_counter

    def __init__(self, connector, make):
        self.__idmouse = Mouse.generate_new_value()
        super().__init__(connector, make)
        inputDevice.__init__(self, connector, make)
    
    def __str__(self):
        return f' the mouse id [ {self.__idmouse}], {super().__str__()}'

    

    
