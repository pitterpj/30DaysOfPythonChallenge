# Exercises - Day 10
# Día 10 - 30DaysOfPythonChallenge

# 💻 Exercises: Day 10
# Iterate 0 to 10 using for loop, do the same using while loop.
num = 0
while num < 10: num +=1; print(num)
# Iterate 10 to 0 using for loop, do the same using while loop.
while num > 0: num -=1; print(num)
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
while num <= 7:
    print(("#") * num)
    num += 1
# Use nested loops to create the following:
num = 0
num2 = 0
while num <= 8:
    print("# " * 9)
    if num2 == 0:
        print("# " * 9)
        num2 += 1
    num += 1  
# Print the following pattern:
num1 = 0
num2 = 0
while num1 != 11:
    print(f"{num1} x {num2} = {num1 * num2}")
    num1 += 1
    num2 += 1
# Use for loop to iterate from 0 to 100 and print only odd numbers
odd = 0
for odd in range(100):
    if odd %2 != 0:
        print(odd)
# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
num = 0
sum_num = 0
for num in range(101):
    sum_num += num
print(sum_num)
# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import data.countries as countries
paises = countries.countries
for pais in paises:
    if "land" in pais:
        print(pais)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits =['banana', 'orange', 'mango', 'lemon']
reverse_fruits = []
for fruit in fruits:
    reverse_fruits.insert(0,fruit)
print(reverse_fruits)
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data

import data.countries_data as total_paises
len_paises = total_paises.data_countries
lenguas_total = set()
lengua_hablada = list()
population = list()
for country in len_paises:
    lenguas_total.update(country['languages'])
    lengua_hablada.insert(0,country['languages'])
    population.insert(0,country['population'])
# Find the 10 most populated countries in the world
population.sort()
population.reverse()
print(population[:10])
# 🎉 CONGRATULATIONS ! 🎉
