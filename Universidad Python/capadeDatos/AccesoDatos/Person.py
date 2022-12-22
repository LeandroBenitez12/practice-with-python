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
    
    def name(self):
        return self._name

    def surname(self):
        return self._surname

    def email(self):
        return self._email

    @name.setter
    def name(self, name):
        self._name = name

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @email.setter
    def email(self, email):
        self._email = email