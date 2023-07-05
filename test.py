### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Lección, llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match = re.match("Esta es la lección", my_string, re.I)
# start, end = match.span()
# print(match)
# print(start)
# print(end)

# print(re.match("Esta es la lección", my_other_string))
# print(re.match("Expresiones regulares", my_string))

search = re.search("es la lección", my_string, re.I)
print(search)
start, end = search.span()
print(start)
print(end)

findall = re.findall("lección", my_string, re.I)
print(findall)

split = re.split(":",my_string)
print(split)