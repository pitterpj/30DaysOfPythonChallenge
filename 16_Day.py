# Exercises - Day 16
# Día 16 - 30DaysOfPythonChallenge
### List comprehension ### 

# 💻 Exercises: Day 16
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
possitive = [i for i in numbers if i<=0]
# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#Not Today
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Using list comprehension create the following list of tuples:
list_tuples = [(i**0, i**1, i**2, i**3) for i in range(11)]
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
output = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country , city in sublist]
print(output)
# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(output)

# 🎉 CONGRATULATIONS ! 🎉