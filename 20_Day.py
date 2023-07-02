# Exercises - Day 20
# Día 20 - 30DaysOfPythonChallenge
### File Handling ###

# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
file_path = "data/obama_speech.txt"
line_count = 0
word_count = 0
with open(file_path, "r") as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)

print("Number of lines:", line_count)
print("Number of words:", word_count)
# b) Read michelle_obama_speech.txt file and count number of lines and words
michelle = "data/michelle_obama_speech.txt"
lines_count = 0
words_count = 0
with open(michelle,"r") as file:
    for line in file:
        lines_count +=1
        words = line.split()
        words_count += len(words)
print("Number of lines:", lines_count)
print("Number of words:", words_count)
# c) Read donald_speech.txt file and count number of lines and words
donald = "data/donald_speech.txt"
linea_count = 0
palabra_count = 0
with open(donald ,"r") as archivo:
    for linea in archivo:
        linea_count +=1
        palabra = line.split()
        palabra_count += len(palabra)

print("Number of lines:", linea_count)
print("Number of words:", palabra_count)
# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def find_top_10_languages():
    with open("data/countries_data.json", "r") as file:
        data = json.load(file)

    languages_count = {}

    for country in data:
        languages = country["languages"]
        for language in languages:
            if language in languages_count:
                languages_count[language] += 1
            else:
                languages_count[language] = 1

    top_10_languages = sorted(languages_count, key=languages_count.get, reverse=True)[:10]

    return top_10_languages

# Call the function
top_languages = find_top_10_languages()

# Print the results
print("Top 10 most spoken languages:")
for index, language in enumerate(top_languages, start=1):
    print(f"{index}. {language}")

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]
# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))

# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]
# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
# Find the 10 most repeated words in the romeo_and_juliet.txt
# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript