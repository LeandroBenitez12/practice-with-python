from Connection import Connection
from Logger_base import log

# se encarga de liberar las conexiones que ya no usemos y regresar al pool de conexiones
class poolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('We enter the method "__enter__"')
        self._connection = Connection.getConnection()    #SOLICITAMOS UN OBJETO CONEXION, de aqui se obtiene un objeto cursor
        self._cursor = self._connection.cursor()  #SOLICITAMOS UN OBJETO CURSOR
        return self._cursor
    #CUANDO TERMINAMOS EL BLOQUE WITH
    #se hace commit o rollback dependiendo de como salio la tranferencia
    def __exit__(self, type_except, value_except, traceback_except):   #traceback = detalle
        log.debug('We enter the method " __exit__" ')
        if value_except:    #Si sale algo es por un error que se debe imprimir y nose guarda nada en la bd
            self._connection.rollback()
            log.error(f'An ocurred Exception: {type_except} {value_except} {traceback_except}')
        else:
            self._connection.commit()   #guardamos todos los cambios
            log.debug('Commit was done correctly')
            self._cursor.close() 
            Connection.returnConnection(self._connection)
            
if __name__ == '__main__':
    with poolCursor() as cursor:
        log.debug('We enter the  with')
        cursor.execute('SELECT * FROM person ') #CUANDO TERMINA ESTO SE MANDA ALLAMAR EL __EXIT__
        log.debug(cursor.fetchall())
