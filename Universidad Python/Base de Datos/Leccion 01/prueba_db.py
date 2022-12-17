import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)
try:
    with conexion:  #para asegurar que se cierre cualquier recuerso asociado a conecion se cierre
        #cursor es un obejto que nos permite ejecutar sentencias SQL en postgres
        with conexion.cursor() as cursor:
            #sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #recuperar un registro 
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #recuperar varios registros
            
            #id_persona = int(input('Ingrese el id_persona: ')) #para un registro
            #llaves_primarias = ((1,2,3),)
            entrada = input('Ingrese los id\'s a buscar(separados por comas):' )
            llaves_primarias = (tuple(entrada.split(',')),)#EL SPLIT SACA LAS , y convertimos los numeros en tupla los ponemos en parentesis y hacemos otra tuplado de esa tupla 
            
            #cursor.execute(sentencia, '''(id_persona,)''') #la ',' es para que sea una tupla y no una simple variable
            cursor.execute(sentencia, llaves_primarias)
            
            registros = cursor.fetchall()   #regresa todos los registros
            #registro = cursor.fetchone()   #regresa un registro queda bien con lo de id_persona = %S ya que es nomas un registro
            
            print(registros)
            #estamos conectados exitosamente a la base de datos
except Exception as e:
    print(f'Error by {e}')
finally:
    #ahora cerramos la conexion
    cursor.close()
    conexion.close()