"""
Continuously ask user to enter number until user enters -1.
When user enters -1 then program should stop asking to enter number.
Calculate and display average of all user entered numbers except -1.
"""

user_input_value = 0
total_of_user_entered_numbers = 0
number_count = 0

# Run while loop until user enters -1
while user_input_value != -1:
    try:
        # Prompt user to enter a number
        user_input = float(input("Please enter a number"))
        if user_input == -1:
            print("Program Terminated")
            user_input_value = -1
        else:
            total_of_user_entered_numbers += user_input
            number_count += 1
    except Exception:
        print("Please enter valid number only")

# Calculate Average of user entered numbers
avg_of_entered_numbers = 0 if number_count == 0 else \
    round(total_of_user_entered_numbers/number_count, 2)

# Display value of avg_of_entered_numbers
print(f"Average of your entered numbers is: {avg_of_entered_numbers}")
