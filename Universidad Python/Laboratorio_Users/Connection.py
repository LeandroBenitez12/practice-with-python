from Logger_base import log
from psycopg2.pool import SimpleConnectionPool
import sys

#se encarga de crear el objeto de pool de conexiones
class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin' 
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1
    _MAX_CONN = 3
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = SimpleConnectionPool(  cls._MIN_CONN, cls._MAX_CONN,
                host = cls._HOST,
                user = cls._USERNAME,
                password = cls._PASSWORD,
                port = cls._DB_PORT,
                database = cls._DATABASE
                )
                log.debug(f'The pool was Created succesfully: {cls._pool}')
                return cls._pool
    
            except Exception as e:
                log.error(f'Ocurrio un Error mientras se obtenia el POOL [{e}]')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connect = cls.getPool().getconn()
        log.debug(f'The connection was correct: {Connection}')
        return connect
    
    @classmethod
    def returnConnection(cls,Connection):
        cls.getPool().putconn(Connection)
        log.debug(f'The connection was returned succesfully: {Connection}')

    @classmethod
    def closeConnection(cls):
        cls.getPool().closedall()

if __name__ == '__main__':
    conex1 = Connection.getConnection()
    Connection.returnConnection(conex1)
    conex2 = Connection.getConnection()
    conex3 = Connection.getConnection()
    conex4 = Connection.getConnection()