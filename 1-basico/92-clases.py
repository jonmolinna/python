# Clases

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.__surname = surname  # propiedad privada

    def fullName(self):
        print(f"{self.name} {self.__surname}")

    # Getters
    def get_surname(self):
        return self.__surname


my_person = Person("Kendra", "Contreras")
# print(my_person.surname)
my_person.fullName()
print(my_person.get_surname())
