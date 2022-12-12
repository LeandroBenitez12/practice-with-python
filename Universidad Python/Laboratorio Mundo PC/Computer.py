from Mouse import Mouse
from Keyboard import Keyboard
from Display import Display

class Computer:
    computer_counter = 0
    @classmethod
    def sumador(cls):
        cls.computer_counter += 1
        return cls.computer_counter

    def __init__(self, name, mouse, keyboard, display):
        self._id_computer = Computer.sumador()
        self._name = name
        self._mouse = mouse
        self._keyboard = keyboard
        self._display = display

    def __str__(self):
        return f''' 
         Computer is: {self._name}: id [{self._id_computer}]
         Mouse: {self._mouse}
         Keyboard: {self._keyboard}
         Display: {self._display}
         '''

if __name__ == '__main__':
    Mouse1  = Mouse('USB 2.0', 'Genius')
    Keyboard1 = Keyboard('USB 3.0', 'Logitech')
    Display1 = Display('PHILIPS', '1024 x 1050')
    Computer1 = Computer('GABRIEL', Mouse1, Keyboard1, Display1)

    print(Computer1)