class Manager_recursos:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Obtenemos recurso'.center(50,'-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name

    def __exit__(self, exc_type, exc_value, trace):
        print('cerramos el recurso'.center(50, '-'))
        if self.name:
            self.name.close()