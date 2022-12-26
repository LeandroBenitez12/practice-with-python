from Conexion import Conexion
from Person import Person
from Logger_base import log
class personaDAO:
    _SELECT = 'SELECT * FROM Person ORDER BY id_person '
    _INSERT= 'INSERT INTO Person( name, surname, email) VALUES( %s, %s, %s)'
    _CREATE =  'SELECT * FROM Person CREATE '
    _UPDATE =   'UPDATE Person SET name = %s, surname = %s, email = %s WHERE id_person = %s'
    _DELETE =   'DELETE FROM Person WHERE id_person = %s'

    @classmethod 
    def select(cls):
        with Conexion.get_cursor() as cursor:
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            persons = []
            for register in registers:
                persona = Person(register[0],register[1],register[2],register[3])
                persons.append(persona)
                return persons
    @classmethod 
    def insert(cls, person):
        with Conexion.get_conexion() as conexion:
            with Conexion.get_cursor() as cursor:
                values = (person.name , person.surname, person.email)
                cursor.execute(cls._INSERT, values)
                log.debug(f'Insert Person: {person}')
                return cursor.rowcount
    
    @classmethod 
    def update(cls, person):
        with Conexion.get_conexion() as conexion:
            with Conexion.get_cursor() as cursor:
                Values= (person.name , person.surname, person.email, person.id_person)
                cursor.execute(cls._UPDATE, Values)
                log.debug(f'persons actualizada: {person}')
                return cursor.rowcount
         
    @classmethod 
    def delete(cls, person):
        with Conexion.get_conexion() as conexion:
            with Conexion.get_cursor() as cursor:
                value = (person.id_person,)
                cursor.execute(cls._DELETE, value)
                log.debug(f'person eliminated:  {person}')
                return cursor.rowcount 


if __name__ == '__main__':
    #DELETE PERSON
    '''persona_eliminada = int(input('Ingrese el id_person a eliminar :   '))
    person_delete1 = Person(id_person= persona_eliminada)
    personas_eliminadas = personaDAO.delete(person_delete1)
    log.debug(f'las personas eliminadas son:    {personas_eliminadas}')'''


    #UPDATE person
    '''person_update1 = Person(name='mapache',surname='jere',email='mpache@hddajd.coms' ,id_person=1)
    persons_updates = personaDAO.update(person_update1)
    log.debug(f'the person actulized :  {persons_updates}')'''
    #INSERT person
    person1 = Person(name='juan',surname='benitez',email='juansvae@gmail.com')
    person2 = Person(name='juana',surname='benitez',email='juanabb@gmail.com')
    
    personas_insertadas = personaDAO.insert(person1)
    log.debug(f'Persons inserted successfully: {personas_insertadas}  ')
    #SELECT person
    '''persons = personaDAO.select()
    for person in persons:
        log.debug(person)'''
        
