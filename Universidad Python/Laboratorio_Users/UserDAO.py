from Connection import Connection
from Users import Users
from Logger_base import log
from poolCursor import poolCursor

# contiene los metodos CRUD
class personaDAO:
    _SELECT = 'SELECT * FROM Person ORDER BY id_person '
    _INSERT= 'INSERT INTO Person( name, surname, email) VALUES( %s, %s, %s)'
    _CREATE = 'SELECT * FROM Person CREATE '
    _UPDATE = 'UPDATE Person SET name = %s, surname = %s, email = %s WHERE id_person = %s'
    _DELETE = 'DELETE FROM Person WHERE id_person = %s'

    @classmethod 
    def select(cls):
        with poolCursor() as cursor: #con los metodos de esta clase , __enter__ se hace automaticamente la conexion y se obtiene el cursor
            log.debug('Select Users...')
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            users = []
            for register in registers:
                user = Users(register[0],register[1],register[2],register[3])
                users.append(user)
            return users  
        #retorna la lista de registros de personas que haya
        #al finalizar el bloque with
        #se llama al metodo exit de la clase cursor del pool,
        #esto es por utilizar el with con resource manager
    @classmethod 
    def insert(cls, user):
        with poolCursor() as cursor:
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)
            log.debug(f'The Inserted record is: {user}')
            return cursor.rowcount
    
    @classmethod 
    def update(cls, user):
        with poolCursor() as cursor:
            Values= (user.username, user.password, person.id_user)
            cursor.execute(cls._UPDATE, Values)
            log.debug(f'The update record is: {user}')
            return cursor.rowcount
         
    @classmethod 
    def delete(cls, user):
        with poolCursor() as cursor:
            value = (user.id_person,)
            cursor.execute(cls._DELETE, value)
            log.debug(f'The deleted record is: {user}')
            return cursor.rowcount 
