from Vehicle import *

class Cleta(Vehicle):
    def __init__(self, type, color , wheels):
        super().__init__( color , wheels)
        self.type = type
    def __str__(self):
        return f'Cleta: type: {self.type}, color: {self.color}, and wheels {self.wheels}'
        