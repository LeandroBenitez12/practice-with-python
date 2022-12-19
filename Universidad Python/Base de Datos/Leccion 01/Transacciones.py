import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)

try:
    conexion.autocommit = False    #valor default, pero lo agregamos popr las dudas
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (name, email) VALUES(%s, %s)'
    valores = ('Leandro', 'Leanbenitz@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET name=%s, email = %s WHERE id_persona = %s'
    valores = ('josema', 'Jimenes@gmail.com', 43)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termino la transacción, se hizo commit ')
except Exception as e:
    conexion.rollback()
    print(f'Error by, se hizo rollback, {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()