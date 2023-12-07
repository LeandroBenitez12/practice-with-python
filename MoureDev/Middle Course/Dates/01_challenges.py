### challenges ###

def calculate(dividendo = 1, divisor = 1):
    return bool(dividendo % divisor) 
num_inicio= 1
num_final = 101
for i in range(num_inicio, num_final):
    if (calculate(i,3) == False and calculate(i,5) == False):
        print("FuzzBizz")
    elif(calculate(i,3) == 0):
        print("Buzz")
    elif(calculate(i,5) == 0):
        print("Fizz")
    else:
        print(i)


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
word_one = str(input('Write a word: '))
word_two = str(input('Write a word: '))

def is_anagram(word_one, word_two):
    word_one = word_one.lower()
    word_two = word_two.lower()

    if word_one == word_two:
        return print(f" The words {word_one} and {word_two} are the same")
    elif( sorted(word_one) == sorted(word_two)):
        return print(f" The words {sorted(word_one)} and {sorted(word_two)} are anagrams")
    else:
        print(f" The words {sorted(word_one)} and {sorted(word_two)} aren't anagrams")
    
is_anagram(word_one, word_two)