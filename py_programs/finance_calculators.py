import math

# Define a message to user
options = """
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:\n
"""
# Prompt user to input type of calculation they want to do
user_choice = input(options)

right_choice = False

# Run while loop until user selects either 'investment' or 'bond'
while not right_choice:

    # Run this if user selects investment
    if user_choice.lower() == "investment":

        deposit_amount = float(input("How much money do you want to \
                                     deposit?\n"))
        interest_rate = float(input("What is the interest rate \
                                    do you want?\n"))/100
        years = int(input("How many years are you planning to invest?\n"))

        interest = input("Do you want 'simple' or 'compound' interest?\n")
        interest_choice = False

        # Run while loop until user selects either 'simple' or 'compound'
        while not interest_choice:
            # Calculate and display total amount if simple interest selected
            if interest.lower() == "simple":
                total_amount = deposit_amount * (1 + interest_rate * years)
                print(f"If you invest £{deposit_amount} on "
                      + f"{interest_rate * 100}% "
                      + f"interest rate for {years} years then with Simple "
                      + f"interest, total you will get £{total_amount}")
                break
            # Calculate and display total amount if compound interest selected
            elif interest.lower() == "compound":
                total_amount = round(deposit_amount *
                                     math.pow((1 + interest_rate), years), 2)
                print(f"If you invest £{deposit_amount} on "
                      + f"{interest_rate * 100}% "
                      + f"interest rate for {years} years then with Compound "
                      + f"interest, total you will get £{total_amount}")
                break
            # Run this if user doesn't select either 'simple' or 'compound'
            else:
                interest = input("Please select either 'simple' or 'compound' "
                                 + "to continue\n")
        break
    # Run this if user selects bond
    elif user_choice.lower() == "bond":
        house_value = float(input("What is the present value of House?\n"))
        interest_rate = float(input("What interest rate you are \
                                    looking for?\n"))/100
        months = int(input("How many months you need to repay total bond?"))
        # Calculate monthly repayment
        formula = ((interest_rate/12) * house_value)\
            / (1 - (1 + (interest_rate/12))**(-months))
        repayment = round(formula, 2)
        print(f"You need to pay £{repayment} every month")
        break
    # Run this if user does not select either 'investment' or 'bond'
    else:
        print("Please enter either 'investment' or 'bond' to continue")
        user_choice = input(options)
