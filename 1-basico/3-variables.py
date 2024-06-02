# Ejericio 1
# Crea un variable con el precio de un juguete que es 15
# Muestra en pantalla su valor
# El precio baja a 12. Asigna el nuevo valor a la variable que has creado
# Muestra el nuevo valor por pantalla
price = 15
print(price)

price = price - 12
print(price)

# Ejercicio 2
# Crea una variable caramelos con valor 5
# crea una variable precio con valor 2
# Crea otra variable que calcule el coste de comprar los caramelos
# Muestra el valor del coste por pantalla
caramelos = 5
price = 2
coste = caramelos * price
print(coste)

# Cambia el valor de caramelos a 8
# cambia el precio a 3
# calcule el nuevo coste
# Muestralo por pantalla
caramelos = 8
price = 3
coste = caramelos * price
print(coste)

# Ejercicio 3
# Tenemos 15 soles de ahorros
# Nuestro abuelo nos da 10
# Nos gastamos 2 euros en un helado
# Nuestra tia nos da 5
# Nos gastamos 7 euros en un juego
# ¿Cuanto dinero tendremos?
ahorro = 15
ahorro = ahorro + 10
ahorro = ahorro - 2
ahorro = ahorro + 5
ahorro = ahorro - 7

print(ahorro)

# Ejercicio 4
# Partimos de :
ahorros = 15
ingresos = 0
gastos = 0

# Nuestro abuelo nos da 10 euros gastamos 2 euros en un helado, Por ayudar al vecino
# nos da 8 euros nos compramos un libro por 12 euros nuestra tia nos da 5 euros
# gastamos 7 euros en un juego
# ¿cuando de ahorro tendremos?
ingresos = ingresos + 10
gastos = gastos + 2
ingresos = ingresos + 8
gastos = gastos + 12
ingresos = ingresos + 5
gastos = gastos + 7

ahorros = ahorros + ingresos - gastos
print(ahorros)

# Ejercicio 5
# Alumnos = 30
# sillas = 50
# aula_completa = alumnos == sillas
alumnos = 30
sillas = 50
aula_completa = alumnos == sillas
print(aula_completa)

nuevos_alumnos = 20
alumnos = alumnos + nuevos_alumnos
aula_completa = alumnos == sillas
print(aula_completa)

# Ejercicio 6
# En un juego hay que conseguir 100 puntos entre 2 niveles de que consta:
# En el nivel 1 tenemos 48 puntos, en el nivel 2 tenemos 62 puntos
# Calcule los puntos totales conseguidos en el juego

# Crea una variable cuyo valor sea el resultado de comparar si los puntos totales conseguidos
# son mayor o igual que los puntos a conseguir
# Muestra el valor de la variable por pantalla
nivel_1 = 48
nivel_2 = 62

resultado = nivel_1 + nivel_2 >= 100

# Ejercicio 7
# Nos dan un dato: 3 dias
# Convertir este dato a horas y luego a minutos
dias = 3
horas = 24 * 3
minutos = horas * 60

print({"dias": dias, "horas": horas, "minutos": minutos})

# Ejercicio 8
# Cambiar el valor de una variable por el valor de la otra
juan = 200
maria = 15

cambio = 200
juan = maria
maria = cambio
print({"Juan ":juan, "Maria": maria})


kendra, noah = 200, 15
kendra, noah = noah, kendra

print({"Noah": noah, "Kendra": kendra})