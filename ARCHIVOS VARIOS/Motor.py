class Motor:
    def __init__(self, motor1, motor2 ):
        self.motor1 = motor1
        self.motor2 = motor2
    def __str__(self):
        return f'Motor: Canal 1: {self.motor1}, Canal 2: {self.motor2}'          
class Robot(Motor):
    def __init__(self, laberinto, motor1, motor2):
        super().__init__(motor1, motor2)
        self.laberinto = laberinto

robot1 = Robot("BoverJR", 23, 32)
print(robot1)