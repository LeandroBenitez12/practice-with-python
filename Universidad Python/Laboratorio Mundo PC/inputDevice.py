class inputDevice:
    def __init__(self,connector, make):
        self._connector = connector
        self._make = make
    def __str__(self):
        return f' The connector is: {self._connector}, the make is: {self._make} '
    @property 
    def connector(self):
        return self._connector

    @connector.setter
    def connector(self, connector):
        self._connector = connector

