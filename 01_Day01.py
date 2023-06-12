# Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# Check the data types of the following data:
print(type(17)) #integer
print(type(6.8)) #float
print(type(3.14)) #float
print(type(7-3j)) #complex
print(type(['Egipto','Python','Chanchito Feliz'])) #list
print(type('Pitter')) #str

#Find an Euclidian distance between (2, 3) and (10, 8)
# Forma 1
from math import sqrt # para poder usar sqrt
print(sqrt((2-10)**2 + (3-8)**2))

# Forma 2 más visual
p = (2, 3) 
q = (10, 8)
r=sqrt((p[0]-q[0])**2 + (p[1] - q[1])**2)
print(r)