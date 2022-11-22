class Vehicle:
    def __init__ (self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return f'Vehicle: color: {self.color}, wheels: {self.wheels}'
