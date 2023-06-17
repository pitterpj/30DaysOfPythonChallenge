# Exercises - Day 6
# Día 6 - 30DaysOfPythonChallenge

### Tuplas ###
# Create an empty tuple
my_tuple =tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
hermano=("hermano1","hermano2")
hermana=("hermana1","hermana2")
# Join brothers and sisters tuples and assign it to siblings
family=hermano+hermana
# How many siblings do you have?
len(family)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=("papa","mama")
family_members=hermana+hermano+parents
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("manzana","tomate","naranja")
vegetables=("calabacín","berenjena")
animales=("perro","gato")
conjunto=fruits+vegetables+animales
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice_tuple=conjunto[3:9]
# Slice out the first three items and the last three items from food_staff_lt list
slice_tuple=conjunto[-3:]
# Delete the food_staff_tp tuple completely
del slice_tuple
# Check if an item exists in tuple:
conjunto.count("items")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
nordic_countries.index("Estonia")
# Check if 'Iceland' is a nordic country
nordic_countries.index("Iceland")

print(slice_tuple)
print(type(conjunto))