from Vehicle import *

class car(Vehicle):
    def __init__(self, speed, color , wheels):
        super().__init__(color , wheels)
        self.speed = speed
    def __str__(self):
        return f'car: speed(km/h){self.speed}, color: {self.color}, and wheels {self.wheels}'
