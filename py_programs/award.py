# Prompt user to enter minutes took to complete Swimming
# and store the value in swimming variable
swimming = int(input("How many minutes took to complete Swimming?"))

# Prompt user to enter minutes took to complete Cycling
# and store the value in cycling variable
cycling = int(input("How many minutes took to complete Cycling?"))

# Prompt user to enter minutes took to complete Running
# and store the value in running variable
running = int(input("How many minutes took to complete Running?"))

# Calculate total time taken by person to complete Triathlon
total_time_of_triathlon = swimming + cycling + running

# print total time of Triathlon
print(f"You took {total_time_of_triathlon} minutes to complete triathlon")

# print the output based on total minutes took to complete Triathlon
if 0 <= total_time_of_triathlon <= 100:
    print("You won Provincial Colours award!")
elif 101 <= total_time_of_triathlon <= 105:
    print("You won provincial Half Colours award!")
elif 106 <= total_time_of_triathlon <= 110:
    print("You won Provincial Scroll award")
else:
    print("Sorry! you didn't win any award!")
