class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    def __str__(self):
        return f' The employee is {self._name}, and receives {self._salary} '

    def show_detail(self):
        return self.__str__()