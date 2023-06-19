# Exercises - Day 9
# Día 9 - 30DaysOfPythonChallenge

# 💻 Exercises: Day 9
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
elif age < 18:
    years = 18 - age
    print(f"You are young. You need to wait {years} more years.")
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 29
difference = my_age - age
if difference == 0:
    print("Somos de la misma edad")
elif difference > 0 and difference == 1:
    print(f"Tenemos una diferencia de {difference} año")

elif difference > 0:
    print(f"Tenemos una diferencia de {difference} años")

elif difference < 0 and difference == -1:
    print(f"Tenemos una diferencia de {-(difference)} año")  

else :
    print(f"Tenemos una diferencia de {-(difference)} años")   
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Introduce numero A: '))
b = int(input('Introduce numero B: '))
if a == b:
    print("Son iguales")
elif a > b:
    print("A es mayor que B")
else:
    print("B es mayor que A")
# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
nota = int(input("Introduce la nota del alumno: "))
if nota > 100 or nota < 0:
    print("Nota inválida")
elif nota >= 80 and nota <= 100:
    print("A")
elif nota >= 70 and nota <= 79:
    print("B")
elif nota >= 60 and nota <= 69:
    print("C")
elif nota >= 50 and nota <= 59:
    print("D")
else:
    print("F")
# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
buy = input('Que fruta quieres? ')

if buy in fruits:
    print('That fruit already exist in the list')
else:
    fruits.insert(0,buy)
    print(fruits)
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Pos existe')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
#     Asabeneh Yetayeh lives in Finland. He is married.
# 🎉 CONGRATULATIONS ! 🎉