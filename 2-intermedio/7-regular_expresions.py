import re

# Match
my_string = "Esta es la lección número 7: Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string)
if not (match == None):
    print(match)
    start, end = match.span()
    print(my_string[start: end])


# Search
search = re.search('lección', my_string)
print(search)
start, end = search.span()
print(my_string[start: end])

# findall
findall = re.findall("lección", my_string)
print(findall)
