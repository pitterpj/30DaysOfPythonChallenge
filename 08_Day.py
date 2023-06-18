# Exercises - Day 8
# Día 8 - 30DaysOfPythonChallenge

#  💻 Exercises: Day 8
# Create an empty dictionary called dog
dog=dict()
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':"",'color':"",'breed':"",'legs':0,'age':0}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'student1',
    'last_name':'last_name_student',
    'gender':'masculino/femenino',
    'age':29,
    'marital_status':'soltero/a',
    'skills':{'Python','JS','SQL','Java'},
    'country':'Spain',
    'city':'City_spain',
    'addres':{'Calle':'falsa','numero':123,'cp':10005},
}
# Get the length of the student dictionary
len(student)
# Get the value of skills and check the data type, it should be a list
student_values=list(student['skills'])
# Modify the skills values by adding one or two skills
student['country']='EEUU'; student['skills'].update(['HTML','CSS'])
# Get the dictionary keys as a list
dict_key=student.fromkeys(student)
# Get the dictionary values as a list
dict_values=student.values()
# Change the dictionary to a list of tuples using items() method
to_tuple=list(student.items())
# Delete one of the items in the dictionary
del student['gender']
# Delete one of the dictionaries
del student