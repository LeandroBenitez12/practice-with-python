from inputDevice import inputDevice

class Keyboard(inputDevice):
    keyboard_counter = 0

    @classmethod
    def generate_new_value (cls):
        cls.keyboard_counter += 1
        return cls.keyboard_counter

    def __init__(self, connector, make):
        self.__idkeyboard = Keyboard.generate_new_value()
        super().__init__(connector, make)
        inputDevice.__init__(self, connector, make)
    
    def __str__(self):
        return f' the keyboard id [ {self.__idkeyboard}], {super().__str__()}'

if __name__ == '__main__':
    Keyboard1 = Keyboard('AT', 'CHERRY')
    Keyboard14 = Keyboard('ATe', 'CHERRY')
    Keyboard13 = Keyboard('ATa', 'CHERRY')
    Keyboard23 = Keyboard('ATg', 'CHERRY')
    Keyboard2 = Keyboard('ATt', 'CHERRY')
    Keyboard10 = Keyboard('AT', 'CHERRY')

    print(Keyboard1)