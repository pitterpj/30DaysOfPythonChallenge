### SETS ###

my_set = set()
my_other_set={}

my_other_set = ['Pitter','Pan',29] # Lista
my_other_set = ('Pitter','Pan',29) # Tupla 
my_other_set = {'Pitter','Pan',29} # Set

my_other_set.add("revampedpj")
print(my_other_set)

print("Pitter" in my_other_set)
print("Pittera" in my_other_set)
my_other_set.remove('Pitter')
print(my_other_set)