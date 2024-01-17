"""
This program takes string and converts into following:
1. Convert each character upper and lower respectively in string
2. Convert each word in lower and upper respectively in string
"""
sentence = "I am Learning to manipulate string in python"

alternate_sentence = ""

# for loop to decide character need to be upper or lower based on index
for each in range(len(sentence)):
    if each % 2 == 0:
        alternate_sentence += sentence[each].upper()
    else:
        alternate_sentence += sentence[each].lower()

# Output sentence which contains each character upper and lower respectively
print(alternate_sentence)

# Create a list by splitting the original string
words = sentence.split()
alternate_words = []

# for loop to decide word in list should be lower or upper based on index
for index in range(len(words)):
    if index % 2 == 0:
        alternate_words.append(words[index].lower())
    else:
        alternate_words.append(words[index].upper())

# Create a string by joining the words (list) with space
alternate_words_sentence = " ".join(alternate_words)

# Output sentence which contains alternate word lower and upper
print(alternate_words_sentence)
