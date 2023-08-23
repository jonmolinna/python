# Diccionarios
my_dict = dict()
my_other_dict = {}

my_dict = {
    "Name": "Kendra",
    "LastName": "Contreras",
    "Age": 28,
    "Languajes": {"Python", "JavaScript", "Php"},
}

my_dict["Address"] = "Av. Los jasmines N° 123"

print(my_dict)
print(my_dict["Name"])

# verificando datos
print("Name" in my_dict)

print(my_dict.items())  # muestra clave y valor
print(my_dict.keys())  # muestra clave
print(my_dict.values())  # muestra valor
