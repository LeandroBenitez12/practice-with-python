from Logger_base import log
from psycopg2.pool import SimpleConnectionPool
import sys

#se encarga de crear el objeto de pool de conexiones
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin' 
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1
    _MAX_CONN = 3
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = SimpleConnectionPool(  cls._MIN_CONN, cls._MAX_CONN,
                host = cls._HOST,
                user = cls._USERNAME,
                password = cls._PASSWORD,
                port = cls._DB_PORT,
                database = cls._DATABASE
                )
                log.debug(f'Creaste pool {cls._pool} succesfully ')
                return cls._pool
    
            except Exception as e:
                log.error(f'Ocurrio un Error mientras se obtenia el POOL [{e}]')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_conexion(cls):
        connect = cls.get_pool().getconn()
        log.debug(f'Conexion obtenida del pool: {connect}')
        return connect
    
    @classmethod
    def liberar_conexion(cls,conexion):
        cls.get_pool().putconn(conexion)
        log.debug(f'Regresamos conexion: {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.get_pool().closedall()

if __name__ == '__main__':
    conex1 = Conexion.get_conexion()
    Conexion.liberar_conexion(conex1)
    conex2 = Conexion.get_conexion()
    conex3 = Conexion.get_conexion()
    conex4 = Conexion.get_conexion()