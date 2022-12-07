class Person:
    person_counter = 0

    @classmethod
    def generate_value(cls):
        cls.person_counter += 1
        return cls.person_counter

    def __init__(self, name, age):
        self.id_person = Person.generate_value()
        self.name = name
        self.age = age

    def __str__(self):
        return f' Person [ {self.id_person}, {self.name}, {self.age} ]'

Person1 = Person('Leandro', 28)
Person2 = Person('Juan', 15)
Person3 = Person('Pablo', 28)
Person4 = Person('Juli', 43)

print(Person1)
print(Person2)
print(Person3)
print(Person4)

print(Person.person_counter)