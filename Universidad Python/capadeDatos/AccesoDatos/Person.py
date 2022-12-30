from Logger_base import log
#clase de entidad, para represntar un registro
class Person:
    def __init__(self,id_person = None ,name = None ,surname = None, email = None): #se lo agregamos a todos el none porque te da error
        self._id_person = id_person
        self._name = name
        self._surname = surname
        self._email = email

    def __str__(self):
        return f'\nThe ID [{self._id_person}], is {self._name} {self._surname}, email: {self._email}'

    @property
    def id_person(self):
        return self._id_person
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    person1 = Person(3,'Juan','Perez','jperez@gmail.com')
    log.debug(person1)
    #   Simular un Insert donde no debemos agregar el id
    #debemos especificar el parametro 
    person2 = Person(name ='Leandro',surname='francis', email='franleao@gmail.com') #pàra evitar el error debemos ir a el metodo init y dar un valor de default a el ID
    log.debug(person2)
    #Simular un delete 
    person3 = Person(id_person=4)
    log.debug(person3)