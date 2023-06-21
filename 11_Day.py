# Exercises - Day 11
# Día 11 - 30DaysOfPythonChallenge

# 💻 Exercises: Day 11
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum_num(a,b): return (a+b)
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(r):
    import math
    area = (math.pi * r * r)
    return area
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (* x):
    suma = 0
    for num in x:
        if type(num) != int:
            return "Not a number"
            break
        suma += num
    return suma
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_C ( C ):
    F = (C * 9.5) + 32
    return F
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn ():
    solve = a*x**2 + b*x +c 
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list ( *param):
    for pa in param:
        print(pa)
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
def reverse_list( *param):
    lista = list()
    for par in param:
        lista.insert(0,par)
    return lista
print(reverse_list(1, 2, 3, 4, 5))
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item (lista : list(), x):
    lista.append(x)
    return lista
add_item (food_staff, 'Pepino')
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item (lista : list(), x):
    lista.remove(x)
    return lista
remove_item (food_staff, 'Potato')
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers (num):
    aux = 0
    solve = 0
    while aux <= num:
        solve += aux
        aux += 1
    return solve
# Exercises: Level 2
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if number < 0:
        return None  # Factorial is undefined for negative numbers
    elif number == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty( algo ):
    if not algo:
        return True
    else:
        return False
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True
# Write a functions which checks if all items are unique in the list.
my_list = [1, 2, 3, 4, 5, 5]
def are_unique(lista_to_check):
    return (len(lista_to_check)) == len(set(lista_to_check))
# Write a function which check if provided variable is a valid python variable
#isidentifier()
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# NOT TODAY
# 🎉 CONGRATULATIONS ! 🎉