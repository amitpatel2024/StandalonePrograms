# Prompt user to enter their age and store the value in age variable
age = int(input("Please enter your age"))

# output the message based on age entered by user
if age > 100:
    print("Sorry, You're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")
