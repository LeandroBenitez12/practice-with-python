
PIEDRA = 1
PAPEL = 2
TIJERA = 3

MIN_VALOR = 0
MAX_VALOR = 3
repeticiones = int(input('Introduzca el numero de repeticiones(Impar): '))

for i in range(2, repeticiones):
    repeticiones = repeticiones % 2
resultado= 'Empezemos el juego...'
print(resultado)
id = 0
rondas_ganadas_jugador_1 = 0
rondas_ganadas_jugador_2 = 0

while id < repeticiones:
    dato_jugador_1 = int(input("Ingrese valor para jugador Nº1 (Piedra[1]/Papel[2]/Tijera[3]): "))
    dato_jugador_2 = int(input("Ingrese valor para jugador Nº2 (Piedra[1]/Papel[2]/Tijera[3]): "))

    if dato_jugador_1 and dato_jugador_2 > MIN_VALOR and dato_jugador_1 and dato_jugador_2  <= MAX_VALOR:
        if dato_jugador_1 == dato_jugador_2:
            resultado = 'Empate'
            print(resultado)
        elif dato_jugador_1 == PIEDRA and dato_jugador_2 == PAPEL:
            resultado = 'Ganador de ronda: Jugador Nº2'
            rondas_ganadas_jugador_2 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_2}')

        elif dato_jugador_1 == PIEDRA and dato_jugador_2 == TIJERA:
            resultado = 'Ganador de ronda: Jugador Nº1 '
            rondas_ganadas_jugador_1 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_1}')

        elif dato_jugador_1 == PAPEL and dato_jugador_2 == PIEDRA:
            resultado = 'Ganador de ronda: Jugador Nº1 '
            rondas_ganadas_jugador_1 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_1}')

        elif dato_jugador_1 == PAPEL and dato_jugador_2 == TIJERA:
            resultado = 'Ganador de ronda: Jugador Nº2 '
            rondas_ganadas_jugador_2 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_2}')

        elif dato_jugador_1 == TIJERA and dato_jugador_2 == PIEDRA:
            resultado = 'Ganador de ronda: Jugador Nº2 '
            rondas_ganadas_jugador_2 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_2}')

        elif dato_jugador_1 == TIJERA and dato_jugador_2 == PAPEL:
            resultado = 'Ganador de ronda: Jugador Nº1 '
            rondas_ganadas_jugador_1 += 1
            print(resultado + f', Rondas ganadas acumuludas : {rondas_ganadas_jugador_1}')
        
        id += 1
    else:
        print('Error , no existe la opcion para el numero ingresado')
        
    
    if id == repeticiones :
        if rondas_ganadas_jugador_1 < rondas_ganadas_jugador_2:
            resultado = 'Ganador jugador 2'
        if rondas_ganadas_jugador_1 > rondas_ganadas_jugador_2:
            resultado = 'Ganador jugador 1' 
        if rondas_ganadas_jugador_1 == rondas_ganadas_jugador_2:
            resultado = 'Partida empatada' 
print('')
print(f'El resultado es : {resultado}')

            




