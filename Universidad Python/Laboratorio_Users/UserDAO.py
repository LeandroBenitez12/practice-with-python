from Users import Users
from Logger_base import log
from poolCursor import poolCursor

# contiene los metodos CRUD
class userDAO:
    _SELECT = 'SELECT * FROM Users ORDER BY id_user '
    _INSERT= 'INSERT INTO users( username, password) VALUES( %s, %s)'
    _CREATE = 'SELECT * FROM Users CREATE '
    _UPDATE = 'UPDATE Users SET username = %s, password = %s WHERE id_user = %s'
    _DELETE = 'DELETE FROM Users WHERE id_user = %s'

    @classmethod 
    def select(cls):
        with poolCursor() as cursor: 
            log.debug('Select Users...')
            cursor.execute(cls._SELECT)
            registers = cursor.fetchall()
            usuarios = []
            for register in registers:
                usuario = Users(register[0], register[1], register[2],)
                usuarios.append(usuario)
            return usuarios  
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
            Values= (user.username, user.password, user.id_user)
            cursor.execute(cls._UPDATE, Values)
            log.debug(f'The update record is: {user}')
            return cursor.rowcount
         
    @classmethod 
    def delete(cls, user):
        with poolCursor() as cursor:
            value = (user.id_user,)
            cursor.execute(cls._DELETE, value)
            log.debug(f'The deleted record is: {user}')
            return cursor.rowcount 
if __name__ == '__main__':
    username_var = input('Write the Username: ')
    password_var = input('Write the Password: ')
    user1 = Users(username= username_var)
    usuarios = userDAO.delete(user1)
    for usuario in usuarios:
        log.debug(usuario)