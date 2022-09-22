class Aritmetica:
    """
    DOC STRING  |   class Aritmetica: to add and subtract
    """
    def __init__(self, operacion1, operacion2): #dunder , y self es una referencia al objeto que vamos a operar
        self.operacion1 = operacion1
        self.operacion2 = operacion2
    
    def Add(self):
        return self.operacion1 + self.operacion2
    
    def Subtract(self):
        return self.operacion1 - self.operacion2

    def multiply(self):
        return self.operacion1 * self.operacion2

    def split(self):
        return self.operacion1 / self.operacion2

    

result1 = Aritmetica(2, 7)
result2 = Aritmetica(1, 8)
result3 = Aritmetica(4, 9)
print(f'the result:{result1.Add()} {result2.Subtract()} {result3.split()} {result1.multiply()} {result2.multiply()}')