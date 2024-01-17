# Prompt user to enter a sentence
str_manip = input("Please enter a sentence")

# Find length of str_manip variable
len_of_str_manip = len(str_manip)

# print length of str_manip
print("Length of your sentence is {}".format(len_of_str_manip))

# Find last letter of str_manip
last_letter_of_str_manip = str_manip[-1]

# Replace last_letter_of_str_manip with @ in str_manip and print
print(str_manip.replace(last_letter_of_str_manip, "@"))

# Find last 3 characters of str_manip variable
last_3_char_of_str_manip = str_manip[len_of_str_manip-3: len_of_str_manip]

# Reverse value of last_3_char_of_str_manip
rev_last_3_char_of_str_manip = last_3_char_of_str_manip[::-1]

# print value of rev_last_3_char_of_str_manip
print(rev_last_3_char_of_str_manip)

# Create 5 letter word which made up with first 3 char and last 2 char
# in str_manip
five_letter_word = str_manip[0: 3] + str_manip[len_of_str_manip-2:]

# print five_letter_word
print(five_letter_word)
