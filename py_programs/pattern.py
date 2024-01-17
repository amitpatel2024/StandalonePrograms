"""
This program output the star pattern using if else condition
    combination with single for loop
"""
# Declare a variable to record decrement required
decrement = 2

# For loop to run for 9 times
for each in range(1, 10):
    if each > 5:
        print("*" * (each - decrement))
        decrement += 2
    else:
        print("*" * each)
