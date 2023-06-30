### Higher Order Functions ###

# def sum_two_values(param1, param2):
#     return param1 + param2

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


def sum_two_values_add_value(param1, param2, f):
    return f(param1 + param2)


print(sum_two_values_add_value(5, 2, sum_one))
print(sum_two_values_add_value(5, 2, sum_five))


def sum_ten():
    def add(value):
        return value + 10
    return add
    

##MAP
numbers = [1,2,5,7,9,34,67,86,43]

def mult_two(number):
    return number * 2

my_map = list(map(mult_two, numbers))
print(my_map)


def sum_two(param1, param2):
    return param1 + param2

print(list(map(lambda x: x * 2, numbers)))
print(reduce(sum_two, numbers))