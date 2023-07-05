# Exercises - Day 21
# Día 21 - 30DaysOfPythonChallenge
### Regular Expressions ###

# Exercises: Level 1
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
import re

cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph)
print(cleaned_paragraph)

# Split the paragraph into words
words = cleaned_paragraph.split()

# Count the frequency of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Get the most common word and its frequency
most_common_word = max(word_counts, key=word_counts.get)
frequency = word_counts[most_common_word]

print("The most frequent word is '{}' with a frequency of {}.".format(most_common_word, frequency))

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers using regular expression
numbers = re.findall(r'-?\d+', text)

# Convert numbers to integers
numbers = [int(num) for num in numbers]

# Find the two furthest particles
furthest_particles = sorted(numbers, key=lambda x: abs(x - 0), reverse=True)[:2]

# Calculate the distance between the furthest particles
distance = abs(furthest_particles[0] - furthest_particles[1])

print("The distance between the two furthest particles is", distance)

# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable

def is_valid_python_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable) is not None

#? print(is_valid_python_variable('my_variable'))
# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text by removing special characters
cleaned_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)

# Convert the sentence to lowercase
cleaned_sentence = cleaned_sentence.lower()

# Split the sentence into words
words = cleaned_sentence.split()

# Count the frequency of each word using a dictionary
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Get the three most common words and their frequencies
most_common_words = sorted(word_counts, key=word_counts.get, reverse=True)[:3]

print("The three most frequent words are:")
for word in most_common_words:
    frequency = word_counts[word]
    print(f"'{word}': {frequency}")

# 🎉 CONGRATULATIONS ! 🎉