from Employee import Employee
class Manager(Employee):
    def __init__(self,name , salary, department):
        super().__init__(name, salary)
        
        self._department = department

    def __str__(self):
        return f'The Manager: Department [ {self._department}]{super().__str__()}}'