# Ejercicio 1
edad = int(input("Ingrese tu edad: "))

if (edad >= 18):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad. ")

# Ejercicio 2
# Programa que pida dos numeros que sumen 10 entre los dos
# Si aciertas, que muestre: "Has acertado"
# Si no aciertas, que muestre: "No has acertado"

number1 = int(input("Ingrese un numero 1: "))
number2 = int(input("Ingrese un numero 2: "))

res = number1 + number2 == 10

if res:
    print("Has acertado")
else:
    print("No has acertado")

# Ejercicio 3
# Programa que pide dos numeros distintos
# y que dice cual es el mayor de los dos
print("Ingrese dos numeros distintos")
number1 = int(input("Ingrese un numero 1: "))
number2 = int(input("Ingrese un numero 2: "))

res = number1 > number2

if res:
    print("El numero mayor es: ",  number1)
else:
    print("El numero mayor es: ", number2)

# Ejercicio 4
# Programa que pida tu edad y la edad de un amigo, y que diga cual es el mayor
# se empieza comprobando la condicion de las edades sean iguales
print("Ingresando Edades")
edad1 = int(input("Ingrese primer edad: "))
edad2 = int(input("Ingrese segundo edad: "))

if (edad1 > edad2 ):
    print("Mayor es: ", edad1)
elif (edad1 == edad2):
    print("Ambos son iguales")
else:
    print("Mayor es: ", edad2)


# Ejercicio 5
# Programa que simula una maquina de refrescos
# la maquina dispone de 4 tipos de refrescos
# te pide el  numero de refresco que deseas entre el 1 el 4
# te informa de tu eleccion

print("--------- Refrescos -------------")
eleccion = int(input("Introduce numero: "))

if eleccion == 1:
    print("Has eligido el refresco 1")
elif eleccion == 2:
    print("Has eligido el refresco 2")
elif eleccion == 3:
    print("Has eligido el refresco 3")
elif eleccion == 4:
    print("Has eligido el refresco 4")
else:
    print("No existe ese numero de producto")

# Ejercicio 6
# Programa que pide la edad de una persona
# Si la edad es mayor o igual que 70: "Es un anciano"
# Si la edad es mayor o igual que 25: "Es un adulto"
# Si la edad es mayor o igual que 14: "Es un joven"
# Si es menor de 14: "Es un niño"

print("--------------- Edades -------------")
print()
edad = int(input("Dime la edad de una persona: "))

if edad >= 70:
    print("Es un anciano")
elif edad >= 25 and edad < 70:
    print("Es un adulto")
elif edad >= 14 and edad < 25:
    print("Es un joven")
else:
    print("Es un niño")

# Ejercicio 7
# 8 es igual a 4+4 y a 4*2 pero no a 4*4
print(8 == 4 + 4 and 8 == 4 * 2 and not (8 == 4 * 4))

# Ejercicio 8
# Programa que simule la entrada a una atraccion en un parque de atracciones, y pide la edad
# y el peso en kilos por seguridad, para poder subir tienes que tener mas de 12 años y pesar mas
# de 45 kilos, sino no puedes subir

edad = int(input("Dime los años que tienes: "))
peso = float(input("Dime tu peso en kilos: "))

if edad > 12 and peso > 45:
    print("Puedes Pasar")
else:
    print("No puedes subir")

# Ejercicio 9
# Programa que simule la entrada a una atraccion en un parque de atracciones y pide
# altura en metros y peso en kilos, por seguridad para poder subir tienes que
# medir mas de 1.30 metros o pesar mas de 40.50 kilos, sino no puedes subir
altura = float(input("Dime la altura en metros: "))
peso = float(input("Dime tu peso en kilos: "))

if altura > 1.3 or peso > 40.5:
    print("Puedes pasar")
else:
    print("No puedes pasar")

# Ejercicio 10
# Programa que simule la entrada a una atraccion en un parque de atracciones, y pide la edad
# y el peso en kilos por seguridad, para poder subir tienes que tener mas de 12 años y pesar mas
# de 45 kilos, sino no puedes subir

edad = int(input("Dime los años que tienes: "))

if edad > 12:
    peso = float(input("Dime tu peso en kilos: "))
    if peso > 45:
        print("Puedes subir")
    else:
        print("No puedes subir a la atraccion")
else:
    print("No puedes subir")




