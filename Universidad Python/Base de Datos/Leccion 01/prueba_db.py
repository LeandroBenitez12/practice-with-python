import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)
try:
    with conexion:  #para asegurar que se cierre cualquier recuerso asociado a conecion se cierre
        #cursor es un obejto que nos permite ejecutar sentencias SQL en postgres
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona' #recuperar registros 
            cursor.execute(sentencia)
            registros = cursor.fetchall()   #regresa todos los registros
            print(registros)
            #estamos conectados exitosamente a la base de datos
except Exception as e:
    print(f'Error by {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()
    conexion.close()