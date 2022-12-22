from Logger_base import log
class Person:
    def __init__(self,id_person ,name ,surname, email):
        self._id_person = id_person
        self._name = name
        self._surname = surname
        self._email = email

    def __str__(self):
        return f'The ID [{self._id_person}], is {self._name} {self._surname}, email: {self._email}'

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
