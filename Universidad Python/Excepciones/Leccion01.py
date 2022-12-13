result = None #No tiene value aun
a = 10
b = 0

try:
    result = a/b
except Exception as e:
    print(f'Error processing {e}')


print(f'The Result is: {result}')
print('CONTINUAMOS...')
