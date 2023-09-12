# Challenges
# Challenge 1
"""
Escribe una programa que muestre por consola (con un print) los números
de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión),
sustetuyendo los siguientes:
    - Multiplos de 3 por la palabra "Fizz".
    - Multiplos de 5 por la palabra "Buzz".
    - Multiplos de 3 y de 5 a la vez por la palabra "FizzBuzz".
"""


def fizz_buzz():
    i = 1
    while i < 101:
        if (i % 15 == 0):
            print(i, "FizzBuzz")
        elif (i % 3 == 0):
            print(i, "Fizz")
        elif(i % 5 == 0):
            print(i, "Buzz")
        else:
            print(i)
        i += 1


# fizz_buzz()

# Challenge 2
"""
Escribe una funcion que reciba dos palabras (String) y retorne verdadero o falso (Bool)
segun sean o no anagramas.
    - Un anagrama consiste en formar una palabra reordenados, todas las letras de otra palabra inicial.
    - No hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
    - Ejm. Álvaro - valora, Zara - raza
"""


def anagrama(str1, str2):
    array1 = list(str1.lower())
    array1.sort()
    array2 = list(str2.lower())
    array2.sort()
    print(array1)
    print(array2)


anagrama("Zara", "Raza")
