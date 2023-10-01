from functools import reduce


# Funciones de orden superior
def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(firstNumber, secondNumber):
    return sum_one(firstNumber + secondNumber)


result = sum_two_values_and_add_one(5, 2)
# print(result)


def sum_two_values_and_add_value(a, b, f_sum):
    return f_sum(a + b)


result = sum_two_values_and_add_value(5, 2, sum_five)
# print(result)


# Closures
def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten()
result = add_closure(5)
print(result)

# Built-in  Higher order functions
numbers = [2, 5, 10, 21, 3, 30]


# Map
def multiply_two(number):
    return number * 2


result = list(map(multiply_two, numbers))
print(result)

result = list(map(lambda number: number * 2, numbers))
print(result)


# Filter
def filter_greater_than_ten(number):
    return number > 10


result = list(filter(filter_greater_than_ten, numbers))
print(result)

result = list(filter(lambda number: number > 10, numbers))
print(result)


# Reduce
def sum_two_values(a, b):
    return a + b


result = reduce(sum_two_values, numbers)
print(result)
