from Conexion import Conexion
from Person import Person
from Logger_base import log
from Cursordelpool import CursorDelPool

# contiene los metodos CRUD
class personaDAO:
    _SELECT = 'SELECT * FROM Person ORDER BY id_person '
    _INSERT= 'INSERT INTO Person( name, surname, email) VALUES( %s, %s, %s)'
    _CREATE =  'SELECT * FROM Person CREATE '
    _UPDATE =   'UPDATE Person SET name = %s, surname = %s, email = %s WHERE id_person = %s'
    _DELETE =   'DELETE FROM Person WHERE id_person = %s'

    @classmethod 
    def select(cls):
        with CursorDelPool() as cursor: #con los metodos de esta clase , __enter__ se hace automaticamente la conexion y se obtiene el cursor
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            persons = []
            for register in registers:
                persona = Person(register[0],register[1],register[2],register[3])
                persons.append(persona)
            return persons  
        #retorna la lista de registros de personas que haya
        #al finalizar el bloque with
        #se llama al metodo exit de la clase cursor del pool,
        #esto es por utilizar el with con resource manager
    @classmethod 
    def insert(cls, person):
        with CursorDelPool() as cursor:
            values = (person.name , person.surname, person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'the Inserted record is: {person}')
            return cursor.rowcount
    
    @classmethod 
    def update(cls, person):
        with CursorDelPool() as cursor:
            Values= (person.name , person.surname, person.email, person.id_person)
            cursor.execute(cls._UPDATE, Values)
            log.debug(f'the update record is: {person}')
            return cursor.rowcount
         
    @classmethod 
    def delete(cls, person):
        with CursorDelPool() as cursor:
            value = (person.id_person,)
            cursor.execute(cls._DELETE, value)
            log.debug(f'the deleted record is: {person}')
            return cursor.rowcount 


if __name__ == '__main__':
    #INSERT person
    person1 = Person(name='Gabriel',surname='Benitez', email= 'Hernang@gmail.com')
    person2 = Person(name='jose',surname='benitez',email='felix091213@gmail.com')
    personas_insertadas = personaDAO.insert(person1)
    log.debug(f'the succesfully inserted records were {personas_insertadas}\n')

    #UPDATE person
    person_update1 = Person(name='Juana', surname='Benitez', email='juanabb@live.com.ar', id_person=8)
    persons_updates = personaDAO.update(person_update1)
    log.debug(f'the succesfully updates recors were: {persons_updates}\n')

    #DELETE PERSON
    persona_eliminada = int(input('Ingrese el id_person a eliminar :   '))
    person_delete1 = Person(id_person= persona_eliminada)
    personas_eliminadas = personaDAO.delete(person_delete1)
    log.debug(f'the succesfully deleted records were: {personas_eliminadas}\n')

    #DELETE PERSON
    persona_eliminada = int(input('Ingrese el id_person a eliminar :   '))
    person_delete1 = Person(id_person= persona_eliminada)
    personas_eliminadas = personaDAO.delete(person_delete1)
    log.debug(f'the succesfully deleted records were: {personas_eliminadas}\n')

    #SELECT person
    persons = personaDAO.select()
    for person in persons:
        log.debug(person)


        
