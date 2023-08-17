# Listas
my_list = list()
my_other_list = []

my_list = [27, 1.70, "Kendra", "Contreras"]
my_list_person = ["Kendra", "Meryem", "Dallas", "Kendra", "kimberly", "Emma"]

age, height, name, surname = my_list
print(name)  # Kendra

# Count
print(my_list_person.count("Kendra"))  # 2

# Add un elemento al ultimo de la lista
my_list.append("Black Dallas")

# Add un elemento de acuerdo a la posicion
# [27, 'Dark', 1.7, 'Kendra', 'Contreras', 'Black Dallas']
my_list.insert(1, "Dark")

# Reemplazar un elemento de acuerdo a la posicion
my_list[1] = "Black"

# Delete un elemento
# my_list.remove("Dark")
# print(my_list)

# Invierte los elementos
my_list.reverse()
print(my_list)

# Ordena los items
number_array = [1, 5, 6, 2, 10, 12, 100, 123, 67]
number_array.sort()
print(number_array)
