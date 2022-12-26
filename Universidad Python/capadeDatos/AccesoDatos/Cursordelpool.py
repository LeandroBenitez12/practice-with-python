from Logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion  = None
        self._cursor = None
    #INICIAMOS EL BLOQUE WITH 
    def __enter__(self):
        log.debug('inicio metodo with "__enter__"')
        self._conexion = Conexion.get_conexion()    #SOLICITAMOS UN OBJETO CONEXION
        self._cursor = self._conexion.cursor()  #SOLICITAMOS UN OBJETO CURSOR
        return self._cursor
    #CUANDO TERMINAMOS EL BLOQUE WITH
    #se hace commit o rollback dependiendo de como salio la tranferencia
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):   #traceback = detalle
        log.debug('Dentro del metodo __exit__')
        if valor_excepcion :    #Si sale algo es por un error que se debe imprimir y nose guarda nada en la bd
            self._conexion.rollback()
            log.error(f'Ocurrio una Excepcion: {tipo_excepcion} {valor_excepcion} {traceback_excepcion}')   
        else:
            self._conexion.commit() #guardamos todos los cambios
            log.debug('commit de la transaccion')
            self._cursor.close()
            Conexion.liberar_conexion(self._conexion)