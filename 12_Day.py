# Exercises - Day 12
# Día 12 - 30DaysOfPythonChallenge

### MODULOS ###

# 💻 Exercises: Day 12
# Writ a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
import random 
import string

def random_user_id ():
    all = string.digits + string.ascii_letters
    user_id = "".join(random.choices(all, k=6))
    return user_id
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user ():
    input_a = int(input('numero de caracteres: '))
    input_b = int(input('numero de IDs generados: '))
    aux = 0
    all = string.digits + string.ascii_letters
    while aux <= input_b :
        user_id = "".join(random.choices(all, k= input_a))
        aux += 1
        print(user_id) 
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def generate_colors(tipo, num):
    aux = 0
    all = string.digits + string.ascii_letters[:6]

    if tipo == 'hexa':
        while aux < num:
            color = ""
            color = "".join(random.choices(all, k= 6))
            aux += 1
            color = "#" + color
            print(color)

    if tipo =="rgb":
        while aux < num:
            print(rgb_color_gen())
            aux += 1
# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
random.shuffle(food_staff)
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def generate_numbers():
    numbers = []
    while len(numbers) < 7:
        ram_num = random.randint(0,9)
        if ram_num in numbers:
            numbers.append(ram_num)
    return numbers

ramdon= generate_numbers()
print(random)