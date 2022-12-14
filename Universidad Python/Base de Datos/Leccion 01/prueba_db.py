import psycopg2

conexion = psycopg2.connect(user='postgres1', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)
try:
    with conexion:  #para asegurar que se cierre cualquier recuerso asociado a conecion se cierre
        #cursor es un obejto que nos permite ejecutar sentencias SQL en postgres
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s '
            primeros_valores = input('ingrese los registros ha eliminar:    ')
            valores = (tuple(primeros_valores.split(',')),)
            #valores = ('Juan', 'Miguez', 'juansvae@gamil.com', 5)
            cursor.execute(sentencia, valores)
            #conexion.commit()  GUARDA REGISTRO EN BASE DE DATOS
            registros_delete = cursor.rowcount
            print(f'Registros eliminados: {registros_delete}')

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

#MODIFIED VARIOUS REGISTERS
'''sentencia = ' UPDATE persona SET name =%s, surname = %s, email = %s WHERE id_persona = %s'
            condicion = int(input(
            Ingrese:
             1 para una sola modificacion
             2 para dos nuevas modificaciones
             3 para tres nuevas modificaciones
             ...    ))
            if condicion == 1:
                primeros_valores = input('Ingrese las modificaciones (separada por coma):   ')
                valores = tuple(primeros_valores.split(','))
            if condicion == 2:
                primeros_valores = input('Ingrese las modificaciones (separada por coma):   ')
                segundos_valores = input('Ingrese las modificaciones (separada por coma):   ')
                valores = (
                    tuple(primeros_valores.split(',')),
                    tuple(segundos_valores.split(',')),
                )

            if condicion == 3:
                primeros_valores = input('Ingrese las modificaciones (separada por coma):   ')
                segundos_valores = input('Ingrese las modificaciones (separada por coma):   ')
                terceros_valores = input('Ingrese las modificaciones (separada por coma):   ')
                valores = (
                    tuple(primeros_valores.split(',')),
                    tuple(segundos_valores.split(',')),
                    tuple(terceros_valores.split(',')),
                )
            #valores = ('Juan', 'Miguez', 'juansvae@gamil.com', 5)
            cursor.executemany(sentencia, valores)
            #conexion.commit()  GUARDA REGISTRO EN BASE DE DATOS'''