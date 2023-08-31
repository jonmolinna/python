# Funciones
def my_function():
    print("this is a function")


my_function()


def sumNumber(a, b):
    return a + b


print(sumNumber(12, 10))


def print_texts(*str):
    for element in str:
        print(element)


print_texts("a", "b", "c")
