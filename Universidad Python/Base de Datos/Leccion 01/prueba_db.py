import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)
try:
    with conexion:  #para asegurar que se cierre cualquier recuerso asociado a conecion se cierre
        #cursor es un obejto que nos permite ejecutar sentencias SQL en postgres
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (name, surname, email) VALUES (%s, %s, %s)'
            valores= (
                ('Julio', 'ramones', 'bokec@type.com'),
                ('Gabriel', 'romero', 'sahac@meil.com'),
                ('Ezequiel', 'briasco', 'Jyn@hotmail.com'),
            ) #tuplas de tupla valores

            cursor.executemany(sentencia, valores)
            #conexion.commit()  GUARDA REGISTRO EN BASE DE DATOS
            registros_insert = cursor.rowcount
            print(f'Registros insertados: {registros_insert}')

except Exception as e:
    print(f'Error by {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()
    