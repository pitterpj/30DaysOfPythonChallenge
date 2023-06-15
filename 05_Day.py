# Exercises - Day 5
# Día 5 - 30DaysOfPythonChallenge

### Listas ###

# Declare an empty list
my_list=list()
# Declare a list with more than 5 items
five_list=[1,2,3,4,5,]
# Find the length of your list
len(five_list)
# Get the first item, the middle item and the last item of the list
first=five_list[0]
last=five_list[-1]
middle=five_list[len(five_list)//2]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies=["Facebook", 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the first, middle and last company
middle=companies[len(companies)//2]
# Insert an IT company in the middle of the companies list
companies.insert((len(companies)//2),"IT")
print(companies)
# Join the it_companies with a string '#;  '
joined = "#".join(companies)
# Check if a certain company exists in the it_companies list.
exist= "Apple" in companies
# Sort the list using sort() method
companies.sort()
# Reverse the list in descending order using reverse() method
companies.reverse()
# Slice out the first 3 companies from the list
del companies[:3]
# Remove all IT companies from the list
del companies
# Destroy the IT companies list
# companies.clear()
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=front_end+back_end
full_stack.insert(full_stack.index("Redux")+1,"Python")
full_stack.insert(full_stack.index("Redux")+1,"SQL")
# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort
max_age= ages[-1]
min_age=ages[0]
# Find the average age (sum of all items divided by their number )
average= sum(ages)/len(ages)
# Find the range of the ages (max minus min)
print(max(ages))
print(min(ages))