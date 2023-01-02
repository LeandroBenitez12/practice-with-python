from Connection import Connection
from Logger_base import log

# se encarga de liberar las conexiones que ya no usemos y regresar al pool de conexiones
class poolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'We enter the method __enter__ ')
        self._conn = Connection.getpool()   #SOLICITAMOS UN OBJETO CONEXION, de aqui se obtiene un objeto cursor
        self._cursor = self._conn.cursor()  #SOLICITAMOS UN OBJETO CURSOR
        return self._cursor
    #CUANDO TERMINAMOS EL BLOQUE WITH
    #se hace commit o rollback dependiendo de como salio la tranferencia
    def __exit__(self, type_except, value_except, traceback_except):   #traceback = detalle
        log.debug(f'We enter the method __exit__ ')
        if value_except:    #Si sale algo es por un error que se debe imprimir y nose guarda nada en la bd
            self._conn.rollback()
            log.error('An ocurred Exception: {tipo_excepcion} {valor_excepcion} {traceback_excepcion}')
        else:
            self._conn.commit()   #guardamos todos los cambios
            log.debug('Commit was done correctly')
            self._cursor.close() 
            Connection.returnConnection(self._conn)
            

