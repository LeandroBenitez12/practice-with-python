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
'''    @classmethod 
    def insert(cls, person):
        
    @classmethod 
    def update(cls, person):
        
    @classmethod 
    def delete(cls, person):'''
        
if __name__ == '__main__':
    persons = personaDAO.select()
    for person in persons:
        log.debug(person)