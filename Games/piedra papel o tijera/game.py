
PIEDRA = 0
PAPEL = 1
TIJERA = 2
repeticiones = int(input('Introduzca el numero de repeticiones(Impar): '))
resultado= 'Empezemos el juego...'
print(resultado)
id = 0
count_win_1 = 0
count_win_2 = 0
while id < repeticiones:
    dato_jugador_1 = int(input("Ingrese valor para jugador Nº1 (Piedra[1]/Papel[2]/Tijera[3]): "))
    dato_jugador_2 = int(input("Ingrese valor para jugador Nº2 (Piedra[1]/Papel[2]/Tijera[3]): "))

    if dato_jugador_1 and dato_jugador_2 > 0 and dato_jugador_1 and dato_jugador_2  <= 3:
        if dato_jugador_1 == dato_jugador_2:
            resultado = 'Empate'
            print(resultado)
        elif dato_jugador_1 == PIEDRA and dato_jugador_2 == PAPEL:
            count_win_2 += 1
        elif dato_jugador_1 == PIEDRA and dato_jugador_2 == TIJERA:
            count_win_1 += 1
        elif dato_jugador_1 == PAPEL and dato_jugador_2 == PIEDRA:
            count_win_1 += 1
        elif dato_jugador_1 == PAPEL and dato_jugador_2 == TIJERA:
            count_win_2 += 1
        elif dato_jugador_1 == TIJERA and dato_jugador_2 == PIEDRA:
            count_win_2 += 1
        elif dato_jugador_1 == TIJERA and dato_jugador_2 == PAPEL:
            count_win_1 += 1
        
    id += 1
    if id == repeticiones :
        if count_win_1 < count_win_2:
            resultado = 'Winner jugador 2'
        if count_win_1 > count_win_2:
            resultado = 'Winner jugador 1' 


print(f' The result is : {resultado}')

            




