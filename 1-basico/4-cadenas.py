# Ejercicio 1
res = "* " * 5 + "+" + " *" * 5
print(res)

res = "a" + "b" + "c" < "acb"
print(res)

# Ejercicio 2
nombre = "Kendra"
apellido = "Contreras"

print("Me llamo " + nombre + " " + apellido)

# Ejercicio 3
print("2 + 2 = " + str(2 + 2))
print("2 + 2 =", 2 + int("2"))

# Ejercicio 4
# ¿Como te llamas?
# ¿De donde eres?

# Hola, Nombre, de ciudad
# Encantado de conocerte

name = input('Ingrese sU Nombre: ')
place = input('De donde eres: ')

print(f"Hola, {name}, de {place}")
print("Encantado de conocerte")

# Ejercicio 5
# ¿En que años estamos?
# ¿Cuantos años tienes o vas a cumplir este año?

# Has nacido en el año
year = int(input("¿En que año estamos?: "))
age = int(input("¿Cuantos años tienes o vas a cumplir este año?: "))

print("Has nacido en el año: ", year - age)

# Ejercicio 6
# Calcule la nota media de tres notas
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("To promedio es: ", promedio)

