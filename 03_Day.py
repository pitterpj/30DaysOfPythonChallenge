# Exercises - Day 3
# Día 3 - 30DaysOfPythonChallenge

print("Hola">="Iola") #Aquí se comprueba la ordenación alfabética no la cantidad de caracteres
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("Vamos a calcular el area de un triángulo")
b= float(input("Introduce la base:"))
h= float(input("Introduce la altura:"))
area= 0.5 * b * h
print("El area del triángulo es:", area)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input('Introduce lado a:'))
b = float(input('Introduce lado b:'))
c = float(input('Introduce lado c:'))
perimeter = a+b+c
print(perimeter)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi= 3.14
r = float(input("Introduce el radio"))
area = pi * r**2
print("el area del circulo es:",area)
c= float(2 * pi * r)
print("La circunferencia es:",c)
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
from math import sqrt 
x=[2,6]
y=[2,10]
pendiente = (y[1]-y[0])/(x[1]-x[0])
print(pendiente)
euclidean = sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
print(euclidean)
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x=-3
result = (x**2 + 6*x + 9)
print(result)
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python')!=len('dragon'))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print( ("on" in "python") and ("on" in "dragon"))
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")
# Find the length of the text python and convert the value to float and convert it to string
x=str(float(len('python')))
print(type(x))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num_1=10
num_2=5
par=False
if(num_2%2==0) : par=True
print(par)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = (7//3 == int(2.7))
print(floor_division)
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
input('Introduce el número de horas :')
input('Introduce el precio por hora :')
cash= (40*28)
print("Semanalmente vas a ganar:",cash)
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
year=float( input('Introduce el número de años: ') )
second_in_year= 365*24*60*60
time= year * second_in_year 
print('Una persona puede vivir: ', time)
