# Exercises - Day 18
# Día 18 - 30DaysOfPythonChallenge
### Higher Order Functions ### 

from functools import reduce
from math import sqrt
# Exercises: Level 1
# Use for loop to print each country in the countries list.
countries_list = ['Spain', 'Portugaland', 'Chaina', 'EEUU', 'Mi Casaland', 'eustaquiLand']
  #? for country in countries_list: print(country)
# Use for to print each name in the names list.
names_list = ['Pepe', 'Chanchito', 'Feliz', 'Moure', 's4vi']
#?for name in names_list: print(name)
# Use for to print each number in the numbers list.
numbers_list = [1,2,3,4,5,6,7,8,9]
#? for num in numbers_list: print(num)
# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
country_upper = list(map(str.upper ,countries_list))
#?print(country_upper)
# Use map to create a new list by changing each number to its square in the numbers list
square_numer = list(map(sqrt, numbers_list))
#?print(square_numer)
# Use map to change each name to uppercase in the names list
names_upper = (list(map(str.upper, names_list)))
#?print(names_upper)
# Use filter to filter out countries containing 'land'.
countries_land = list(filter(lambda x:"land" in x,countries_list))
#?print(countries_land)
# Use filter to filter out countries having exactly six characters.
countries_carac = list(filter(lambda x: len(x) == 6, countries_list))
#?print(countries_carac)
# Use filter to filter out countries containing six letters and more in the country list.
countries_carac = list(filter(lambda x: len(x) >= 6, countries_list))
#?print(countries_carac)
# Use filter to filter out countries starting with an 'E'
countries_carac = list(filter(lambda x: x[0] == "E", countries_list))
print(countries_carac)
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chain = list(map(str.upper, filter(lambda x: x[0] == "E", countries_list)))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
all_types = [12, "Chanchito", 12.5, 'Pit', True]
def get_string_list(list_types):
    list_strings = list(filter(lambda x : type(x) == str, list_types))
    return print(list_strings)
#?get_string_list(all_types)
# Use reduce to sum all the numbers in the numbers list.
solve_num = reduce(lambda x, y: x + y, numbers_list)
#?print(solve_num)
countries_list =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import data.countries_data as countries_list
paises = countries_list.data_countries
print(paises)
def categorized_countries(list_to_categorized):
    pattern = 'land'
    list_catg = list(filter(lambda x : pattern in x['name'],list_to_categorized))
    return list_catg
#?print(categorized_countries(paises))
# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
sorted_name = sorted(paises, key=lambda pais : pais['name'])
sorted_capital = sorted(paises, key=lambda pais : pais['capital'])
sorted_population = sorted(paises, key=lambda pais : pais['population'])
print(sorted_capital)
# 🎉 CONGRATULATIONS ! 🎉