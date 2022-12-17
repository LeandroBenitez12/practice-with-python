import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)
try:
    with conexion:  #para asegurar que se cierre cualquier recuerso asociado a conecion se cierre
        #cursor es un obejto que nos permite ejecutar sentencias SQL en postgres
        with conexion.cursor() as cursor:
            sentencia = ' UPDATE persona SET name =%s, surname = %s, email = %s WHERE id_persona = %s'
            primeros_valores = input('Ingrese las modificaciones (separada por coma):   ')
            valores = tuple(primeros_valores.split(','))
            #valores = ('Juan', 'Miguez', 'juansvae@gamil.com', 5)
            cursor.execute(sentencia, valores)
            #conexion.commit()  GUARDA REGISTRO EN BASE DE DATOS
            registros_modified = cursor.rowcount
            print(f'Registros modificados: {registros_modified}')

except Exception as e:
    print(f'Error by {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()
    



#INSERT VARIOUS REGISTERS
'''sentencia = 'INSERT INTO persona (name, surname, email) VALUES (%s, %s, %s)'
            valores= (
                ('Julio', 'ramones', 'bokec@type.com'),
                ('Gabriel', 'romero', 'sahac@meil.com'),
                ('Ezequiel', 'briasco', 'Jyn@hotmail.com'),
            ) #tuplas de tupla valores
'''