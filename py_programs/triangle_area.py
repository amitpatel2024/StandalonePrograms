import math

# Prompt user to enter length of all 3 sides of Triangle
side1 = float(input("Please enter length of first side of Triangle"))
side2 = float(input("Please enter length of second side of Triangle"))
side3 = float(input("Please enter length of third side of Triangle"))

# Calculate Semi-Perimeter of Triangle and store the result in s
s = (side1 + side2 + side3)/2

# Calculate the area of Triangle and round the result with 2 decimal
area = round(math.sqrt(s * (s-side1) * (s-side2) * (s-side3)), 2)

# print the area of Triangle
print("The Area of Triangle is {}".format(area))
