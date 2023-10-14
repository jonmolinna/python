import re

my_string = 'Esta es la lección número 7: Lección llamada Expresiones Regulares'

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

# Buscar leccion o expresiones
pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

# Buscar caracteres numeros o no numericos en string
pattern = r'\d'
print(re.findall(pattern, my_string))

# Busca todas las letras
pattern = r'\D'

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# Email
pattern = r"^[a-zA-Z0-9_.*-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# https://regex101.com/
