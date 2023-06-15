# Exercises - Day 4
# Día 4 - 30DaysOfPythonChallenge

### Strings Format ###

name, surname, age = 'Pitter', 'pan', 29

print("voy a imprimir %s %s y luego edad %d" %(name,surname,age))
print("voy a imprimir {} {} y luego edad {}" .format(name,surname,age))
print(f"voy a imprimir {name} {surname} y luego edad {age}")

# Division
name ="python"
print(name)

slice_name=name[1:3]  # El último caracter no lo pilla
print(slice_name)

# Reverse
reverse_name=name[::-1] # para darle la vuelta al string
print(reverse_name)

# Saltos
jump_name=name[0:6:2] #C oge todo saltando cada dos
print(jump_name)

# Métodos/funciones
print(name.capitalize()) #Poner primera en mayus
print(name.upper()) #
print(name.count("t")) #
print(name.isnumeric()) #
print(name.startswith("P")) #

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concatenate = 'Thirty '+ 'Days ' + 'Of ' + 'Python'
# Change all the characters to uppercase letters using upper() method.
concatenate_upper=concatenate.upper()
# Change all the characters to lowercase letters using lower() method.
concatenate_lower=concatenate.lower()
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
title=concatenate.swapcase()
# Cut(slice) out the first word of Coding For All string.
word= "Coding For All"
slice_word= word[0:6]
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
find_word=word.index("For")
# Replace the word coding in the string 'Coding For All' to Python.
replace=word.replace('string','python')
# Split the string 'Coding For All' using space as the separator (split()) .
split=word.split()
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
phrase= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split=phrase.split()
# What character is at index 10 in "Coding For All" string.
word[11]
# Create an acronym or an abbreviation for the name 'Coding For All'.
words=word.split()
siglas=''.join(word[0].upper() for word in words)
# Use index to determine the position of the first occurrence of C in Coding For All.
index=word.index("C")
# Use index to determine the position of the first occurrence of F in Coding For All.
index=word.index("F")
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
index=word.rfind("l")
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase="You cannot end a sentence with because because because is a conjunction"
slice_phrase= phrase[phrase.index("because"):(phrase.rfind("because"))]
#other
slice2=phrase.split("with ")[1].split(" is")[0]
# Does ''Coding For All' start with a substring Coding?
true=word.startswith('Coding')
# Does 'Coding For All' end with a substring coding?
false=word.endswith('Coding')
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
phrase='   Coding For All      ' 
remove= phrase.strip()
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lists=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
union=' # '.join(lists)
# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
print("The area of a circle with radius %d is %f meters square." %(radius,area))
