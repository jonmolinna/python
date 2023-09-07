# Exceptions
numberOne = 10
numberTwo = "12"

# Try Except Elsem (Opcional) Finally (Opcional)
try:
    def sumNumber(a, b):
        return a + b

    result = sumNumber(numberOne, numberTwo)
    print(result)
except:
    print("Se ha producido un error")
else:  # se ejecuta cuando no se produce error
    print("La ejecucion continua correctamente")
finally:  # se ejecuta siempre
    print("La ejecucion continua")

numberA = 10
numberB = 12


def resNumber(a, b):
    return a - b


result = resNumber(numberA, numberB)
print(result)

# Tipos de errores
numberOne = 10
numberTwo = "12"

try:
    def sumNumber(a, b):
        return a + b

    result = sumNumber(numberOne, numberTwo)
    print(result)
except ValueError as error:
    print("Se ha producido un ValueError")
    print(error)
except TypeError as error:
    print("Se ha producido un TypeError")
    print(error)
except Exception as error:
    print("Se a producido un error Exception")
    print(error)
