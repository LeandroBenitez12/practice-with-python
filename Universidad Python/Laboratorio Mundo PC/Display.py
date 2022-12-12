
class Display:
    Display_counter = 0

    @classmethod
    def generate_new_value (cls):
        cls.Display_counter += 1
        return cls.Display_counter

    def __init__(self, make, size):
        self.__idDisplay = Display.generate_new_value()
        self.__make = make
        self.__size = size
    
    def __str__(self):
        return f' the Display id [ {self.__idDisplay}], The make is: {self.__make}, the size is: {self.__size}'
    
    @property 
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make
        
    @property 
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
