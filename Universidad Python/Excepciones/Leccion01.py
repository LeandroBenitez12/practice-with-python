result = None #No tiene value aun
a = '10'
b = 0

try:
    result = a/b
except ZeroDivisionError as e:#la clase ZeroDivisionError es una clase hija 
    #, una sub clase digamos, si nosotros utilizamos Exception que es la clase padre,
    #ante cualquier error nosotros acutuamos protegiendo de la interrupcion de la app e informando el error

    print(f'Error processing {e}')


print(f'The Result is: {result}')
print('CONTINUAMOS...')
