import random
import os


def run():
    VIDAS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
     /    |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
     / \  | 
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
      |-¬ |
     / \  |
    =========''']
    equipoFulbo = ['BOCA', 'RIVER', 'GIMNASIA', 'SANSILENCIO', 'INDESINGENTE', 'RASINCOPA']
    equipoAdivinar = random.choice(equipoFulbo)

    guioncito = '_'
    guiones = ["_"] * len(equipoAdivinar)
    intentos = 7

    while True:
        os.system("cls")
        for character in guiones:
            print(character, end = ' ')
        print(VIDAS[intentos])
        letraIngresada = str(
            input("Ingresa una letra pedazo de gorreado:  ")).upper()

        encontreLetra = False
        for idx, character in enumerate(equipoAdivinar):
            if character == letraIngresada:
                guiones[idx] = letraIngresada
                encontreLetra = True

        if not encontreLetra:
            intentos -= 1

        if guioncito not in guiones:
            os.system("cls")
            print('GANE')
            break
            input()
        
        if intentos == 0:
            os.system("cls")
            print('Descendiste B|')
            break
            input()


run()
