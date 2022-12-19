import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (name, surname, email) VALUES(%s, %s, %s)'
            valores = ('ZUKITA',  'FEBALLIONE', 'ZUKI78@gmial.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET  name = %s  WHERE id_persona = %s'
            valores = ( 'FAFAFAFAFAFFA' , 48)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Error by, se hizo rollback, {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()

print('Termino la transacción, se hizo commit ')