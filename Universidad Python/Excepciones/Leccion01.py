result = None #No tiene value aun
a = '10'
b = 0

try:
    result = a/b
except ZeroDivisionError as z:#la clase ZeroDivisionError es una clase hija 
    #, una sub clase digamos, si nosotros utilizamos Exception que es la clase padre,
    #ante cualquier error nosotros acutuamos protegiendo de la interrupcion de la app e informando el error
    #lo recomendable es usar las sub clases, o clases hijas , y luego al final por las dudas poner la clase PADRE
    print(f'ZeroDivisionError - Error processing {z}, {type(z)}')

except TypeError as t:
    print(f'TypeError - Error processing: {t}, {type(t)}')

except Exception as e:
    print(f'Exception - Error processing: {e}, {type(e)}')

print(f'The Result is: {result}')
print('CONTINUAMOS...')
