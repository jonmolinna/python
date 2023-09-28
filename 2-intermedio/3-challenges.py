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


def is_anagram(str1, str2):
    if str1.lower() == str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower())


# result = is_anagram("Roma", "Amor")
# print(result)

# Challenge 3
"""
Escrible un programa que imprima los 50 primeros numeros de la sucesion de fibonacci empezando 0.
    - La serie fibonacci se compone por la sucesion de numeros en la que el siguiente siempre
      es la suma de los dos anteriores.
      ejm 0, 1, 1, 2, 3, 5, 8, 13 ....
"""


def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


# fibonacci()

# Challengue 4
"""
Escribe un programa que se encarga de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 100
"""


def is_primo(number):
    if (number == 1):
        return False

    for i in range(2, number):
        if (number % i == 0):
            return False

    return True


def list_primos():
    for index in range(1, 101):
        result = is_primo(index)
        if (result):
            print(index, "Es primo")
        else:
            print(index)


# list_primos()


# Otra forma
def is_prime(number):
    if number < 2:
        return False

    for index in range(2, number):
        if number % index == 0:
            return False

    return True


def list_primos_2():
    for index in range(1, 101):
        result = is_primo(index)
        if (result):
            print(index, "Es primo")
        else:
            print(index)


# list_primos_2()


# Challengue 5
"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones
propias del lenguaje que lo hagan de forma automatica.
- Si le pasamos "Hola mundo" nos retornara "odnum aloh
"""


def invert_str(str):
    my_list = list(str)
    size = len(my_list) - 1
    arr_str = []
    str_ivert = ""

    for index in my_list:
        arr_str.append(my_list[size])
        size = size - 1

    for index in arr_str:
        str_ivert = str_ivert + index

    print(str_ivert)


# invert_str("Hola Mundo")

def reverse(text):
    text_len = len(text)
    reverse_text = ""
    for index in range(0, text_len):
        reverse_text += text[text_len - index - 1]
    return reverse_text


print(reverse("Hola Mundo"))
