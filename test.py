### File handing ###


# .txt file
import os

txt_file = open("my_file.txt", "w+")
txt_file.write("\nMy name is Pitter\n Chanchito Feliz\n Tengo 29 años\nMy lenguaje preferido es Python")

print(txt_file.readline())
txt_file.write("\nAñado una linea nueva")

for line in txt_file.readlines():
    print(line)

txt_file.write("\n Other line")

print(txt_file.readline())

txt_file.close()

#os.remove("my_file.txt")


### JSON

import json

json_file = open("data/my_file.json", "w+")

json_test = {
    "Nombre": "Pitter",
    "Apellido": "Chanchito",
    "Edad": 29,
    "Calle": {"Direccion": "Falsa", "N":  123, "C.P.": 10910}
    }

json.dump(json_test, json_file, indent = 4)

json_file.close()

# with open("data/my_file.json") as chanchito:
#     for line in chanchito.readlines():
#         print(line)

json_dict = json.load(open("data/my_file.json"))
print(type(json_dict))