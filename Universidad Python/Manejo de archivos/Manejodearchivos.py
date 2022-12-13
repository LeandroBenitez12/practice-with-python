try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Add a new information')
    archivo.write('\nAdios')
except Exception as e:
    print(e)
finally:
    archivo.close()