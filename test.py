#### Excepction Handling ###
# Exercises - Day 14
# Día 14 - 30DaysOfPythonChallenge

# 💻Exercises: Day 14
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# . Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
fin,sw,nor,den,ice,*rest=names
nordic_countrie = fin,sw,nor,den,ice
es,ru=rest
print(nordic_countrie)
print(es)
print(ru)
# 🎉 CONGRATULATIONS ! 🎉