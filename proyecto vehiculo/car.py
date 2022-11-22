from Vehicle import *

class car(Vehicle):
    def __init__(self, color , wheels, speed):
        super().__init__(color , wheels)
        self.speed = speed
    def __str__(self):
        return super().__str__() + ', Speed (km/h): ' + str(self.speed)#f'car: speed(km/h){self.speed}, color: {self.color}, and wheels {self.wheels}'
