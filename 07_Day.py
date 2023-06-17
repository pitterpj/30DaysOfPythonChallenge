# Exercises - Day 7
# Día 7 - 30DaysOfPythonChallenge

### SETS ###
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Oracle','Azure','Yendo'])
# Remove one of the companies from the set it_companies
it_companies.pop()
# What is the difference between remove and discard
 # ? Remove se usa para eliminar un elemento del set en concreto y además si no existe ese elemento nos imprimirá por pantalla un KeyError. Discard eliminará un elemento del set y en caso de que no exista no nos dará error, simplemente no ocurrirá nada.  
# Exercises: Level 2
# Join A and B
C=A.union(B)
# Find A intersection B
C=A.intersection(B)
# Is A subset of B
C=A.issubset(B) #True #? subset es que todos los elementos de A existen en B
# Are A and B disjoint sets
C=A.isdisjoint(B) #? Disjuntos es que no tienen elementos en común
# What is the symmetric difference between A and B
C=A.symmetric_difference(B)
# Delete the sets completely
del C
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age=set(age)
answer= len(set_age) < len(age) #? age es más grande porque el set elimina duplicados
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
answer="I am a teacher and I love to inspire and teach people"
split_answer=answer.split()
set_amswer=set(split_answer)