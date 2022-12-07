class Myclass:
    class_variable = ' Hello World '
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    @staticmethod
    def methodStatic():
        print(Myclass.class_variable2)
    @classmethod
    def methodClass(cls):
        print(cls.class_variable2)
        
    def methodInstance(self):
        self.methodClass
        self.methodStatic
        print(self.class_variable)
        print(self.instance_variable)

Myclass.class_variable2 = 'heheheehe'

Myobject1 = Myclass('object1')

Myobject1.methodInstance ()
#Myclass.methodStatic()