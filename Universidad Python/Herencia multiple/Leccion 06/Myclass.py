class Myclass:
    class_variable = ' Hello World '
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    @staticmethod
    def getStatic():
        print(Myclass.class_variable2)
    @classmethod
    def getClass(cls):
        print(cls.class_variable2)
        
Myclass.class_variable2 = 'heheheehe'

Myobject1 = Myclass('object1')

Myobject1.getClass()
#Myclass.getStatic()