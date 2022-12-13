try:
    archivo = open('prueba.txt', 'w', encoding= 'utf8')
    archivo.write('Add a new informatión')
    archivo.write('\nAdios')
except Exception as e:
    print(e)
finally:
    archivo.close()