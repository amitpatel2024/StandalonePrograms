"""
Create a menu list that contains name of items sold in the cafe.
Create a stock dictionary that contains items name and
    quantity of items in the cafe.
Create a price dictionary that contains items name and
    price of items in the cafe.
Calculate total worth of stock present in the cafe.
"""

menu = ["Coffee", "Tea", "Brownie", "Sandwitch", "Slush"]

stock = {"Coffee": 25, "Tea": 15, "Brownie": 8, "Sandwitch": 20, "Slush": 10}

price = {"Coffee": 3.75, "Tea": 3.25, "Brownie": 2.15, "Sandwitch": 4.99,
         "Slush": 2.99}

total_stock = 0

# Run for loop for every item present in menu list
for item in menu:
    # Calculate individual item value by multiplying quantity and value
    item_value = stock[item] * price[item]
    total_stock += item_value

# Output the total stock value in the cafe
print(f"Total stock value in cafe is: £{total_stock}")
