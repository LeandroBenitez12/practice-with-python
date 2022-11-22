from Vehicle import *

class Cleta(Vehicle):
    def __init__(self, color, wheels, type):
        super().__init__( color , wheels)
        self.type = type
    def __str__(self):
        return super().__str__() + ', type : ' + str(self.type)
        