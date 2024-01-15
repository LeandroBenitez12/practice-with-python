'''
Gestor de Tareas (To-Do List):

Crea un programa que permita al usuario agregar, eliminar y marcar como completadas tareas en una lista. 
Puedes implementar funciones como agregar tarea, eliminar tarea, marcar tarea como completada, 
mostrar todas las tareas, etc.
'''
class My_class_task:
    def __init__(self, l, t):
        self.list = list(l)
        self.ticklist = list(t)
    def addTask(self):
        task_to_add = str(input("Ingrese su tarea para agregar:  "))
        list = self.list
        list.append(task_to_add)
        print(f'Se agrego {task_to_add} a la lista y quedo asi: {self.list}')
        
    def deleteTask(self):
        task_to_delete = str(input("Ingrese su tarea para eliminar:  "))
        list = self.list
        if task_to_delete in self.list:
            list.remove(task_to_delete)
            print(f'Se elimino {task_to_delete} de la lista y quedo asi: {self.list}')
        else:
            print("No se encontro el elemento en la lista. ")
        
    def tickTask(self):
        tick = input("Ingrese la tarea completada")
        if tick in self.list:
            self.ticklist.append(tick)
            print(f"Se agrego {tick} a la lista tareas completas, la lista quedo asi: {self.ticklist}")
        else:
            print("No hay elemento coincidente en la lista de tareas para hacer")
         
    def showAllTasks(self):
        print('The tasks are: ')
        for task in self.list:
            print(task)
    

def menu():
    print("-----------Menu-------------")
    print("1. add Task")
    print("2. delete task")
    print("3. tick task")
    print("4. show all Tasks")
    return int(input("Ingrese la opcion en numero:  "))



listCheck = []
           
def program():
    
    ticklist = []
    lista = []
    task_managment = My_class_task(lista, ticklist)
    
    while True:
        opcion = menu()
    
        # condicionales para seleccionar opcion del menu
        if opcion == 1:
            task_managment.addTask()
        elif opcion == 2:
            task_managment.deleteTask()
        elif opcion == 3:
            task_managment.tickTask()
        elif opcion == 4:
            task_managment.showAllTasks()
        else:
            print("Opcion Incorrecta, ingrese nuevamente")
        
        # condicional para finalizar el bucle 
        if input("Desea Continuar: (y/n): ") != 'y':
            break
        
program()