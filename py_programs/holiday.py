"""
Calculate total cost of Holiday for a person.
Prompt user to enter Flight, Hotel and Car Hire details.
Write a function named as 'hotel_cost' which takes 'num_nights' as parameter
    and calculates and return total hotel cost for user based on night charge
    and number of nights they entered.
Write a function named as 'plane_cost' which takes 'city_flight' as paramter
    decides and return total flight
    cost for user based on city they wish to travel to.
Write a function named as 'car_rental' which takes 'rental_days' as parameter
    calculates and return total car hire cost for user based on daily rental
    cost and number of days they entered.
Write a function named with 'holiday cost' which calculates total cost of
    holiday by doing sum of plane_cost, hotel_cost and car_rental cost.
Output the total holiday cost in readable format.
"""

# Create dict which contains index as keys and city names as value
cities = {"1": "london", "2": "glasgow", "3": "cardiff", "4": "edinburgh",
          "5": "belfast"}

# Run while loop until user enters either city or associated index number
while True:
    print()
    city_flight = input("""Which City are you flying to? Enter name or number.

                    1. London
                    2. Glasgow
                    3. Cardiff
                    4. Edinburgh
                    5. Belfast

                    Enter '-1' to cancel the process

                    :""").lower().strip()
    # if user enters city name or index as city_flight then break the loop
    if city_flight in cities.keys():
        city_flight = cities[city_flight]
        break
    elif city_flight in cities.values():
        break
    # Run this if user enters -1
    elif city_flight == str(-1):
        print()
        # Prompt user to enter y/n when enters -1
        user_choice = input("Before you go, Do you want to see the price " +
                            "of flights? (y/n)\n").lower().strip()
        # Here if user enters anything except y or n related then just exit
        if user_choice in ["y", "yes", "yeah", "1"]:
            continue
        elif user_choice in ["n", "no", "nope", "0"]:
            print()
            print("Good Bye!!! See you soon.")
            exit()
        else:
            print("Have a Nice Day.")
            exit()
    else:
        print("Please enter valid city name or index to continue")


# Run while loop until user enters valid number or -1
while True:
    print()
    num_nights = input("How many nights are you planning to stay at Hotel? " +
                       "Enter '0' if you are not planning to stay at Hotel.\n")
    try:
        if num_nights.lower() == str(-1):
            print("Good Bye!!! See you soon.")
            exit()
        num_nights = int(num_nights)
        break
    except (ValueError, Exception):
        print("Please enter valid number to continue or " +
              "enter '-1' to cancel the process.")


# Run while loop until user enters valid number or -1
while True:
    print()
    rental_days = input("How many days do you want to hire a car for?" +
                        " Enter '0' if you don't want to hire a car.\n")
    try:
        if rental_days.lower() == str(-1):
            print("Good Bye!!! See you soon.")
            exit()
        rental_days = int(rental_days)
        break
    except (ValueError, Exception):
        print("Please enter valid number to continue or " +
              "enter '-1' to cancel the process.")


def hotel_cost(num_nights):
    """Count and retrun total hotel cost based on num_nights"""
    price_per_night = 225
    return price_per_night * num_nights


def plane_cost(city_flight):
    """Decide and return plane cost based on city provided"""
    cost_of_flight = 0
    if city_flight == "london":
        cost_of_flight = 350
    elif city_flight == "glasgow":
        cost_of_flight = 200
    elif city_flight == "cardiff":
        cost_of_flight = 100
    elif city_flight == "edinburgh":
        cost_of_flight = 150
    elif city_flight == "belfast":
        cost_of_flight = 410
    else:
        print("Invalid value")
        raise ValueError
    return cost_of_flight


def car_rental(rental_days):
    """Calculate and return total car rental price based on rental_days"""
    daily_rental_cost = 50
    return daily_rental_cost * rental_days


def holiday_cost(hotel_cost, plane_cost, car_rental):
    """Calculates and return total holiday cost, prints the output"""
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    print(f"""
        {"*" * 40}
        YOUR TOTAL HOLIDAY COST WILL BE £{total_holiday_cost}

        See the breakdown as below:
        {"-" * 40}
        Services               Total Price in £
        {"-" * 40}
        Flight                    {plane_cost}
        Hotel                     {hotel_cost}
        Car                       {car_rental}
        {"*" * 40}
        """)
    return total_holiday_cost


# Call the holiday_cost function by passing functions as arguments
holiday_cost(hotel_cost(num_nights), plane_cost(city_flight),
             car_rental(rental_days))
