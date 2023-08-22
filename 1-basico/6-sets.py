# SETS
# Un set no es una estructura ordenada
# Un set no admite repetidos
my_set = set()
my_other_set = {}  # inicialmente es un diccionario

my_set = {"Kendra", "Contreras", 27}

# Add un elemente al set
my_set.add('Dallas')
print(my_set)

# Buscando un elemento en los sets
print("Kendra" in my_set)  # true

# Convertir un set a una lista
my_list = list(my_set)
print(my_list)
