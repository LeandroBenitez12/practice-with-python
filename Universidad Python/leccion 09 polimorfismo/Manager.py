from Employee import Employee
class Manager(Employee):
    def __init__(self,name , salary, department):
        super().__init__(name, salary)
        
        self._department = department

    def __str__(self):
        return f'{super().__str__()}, He/She is a Manager and is in the Department of: [{self._department}]'