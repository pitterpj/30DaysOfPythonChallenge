# Exercises - Day 12
# Día 12 - 30DaysOfPythonChallenge

# 💻 Exercises: Day 12
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i <= 0] 
# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
unique_list = [element for sublist in list_of_lists for subsublist in sublist for element in subsublist]
# Using list comprehension create the following list of tuples:
result = [(0 + i ,1 ,0 + i ,i * i, i **3,i **4) for i in range(11)]
for tuple in result: print(tuple)
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

