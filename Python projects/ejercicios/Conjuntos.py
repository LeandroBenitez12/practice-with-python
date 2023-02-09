A = {1,2,3,4}
B = {2,3,5,6}
C = {3,4,6,7}

nucleo = A&B&C # compara y imprime el que esta en todos
une = A|B|C #une todos los numeros sin repetir
distintos= A^B^C #
#print(distintos) #los que cada Redondo tiene y no comparte + el nucleo

for i in une:
    print(f'los nº que se unen sin repetir son: {i}')

for i in nucleo:
    print(f'los nº que se repiten en todos son: {i}')

for i in distintos:
    print(f'los nº que no comparten con ninguno son: {i}')