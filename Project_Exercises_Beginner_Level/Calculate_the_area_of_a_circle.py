import math


def calculate_area(radius):
    return math.pi * radius ** 2


radius = float(input("What is the radius? "))

output = calculate_area(radius)
print("The area of a circle with the radius " + str(radius) + " is " + str(output))
print(f"Or to two decimal places it is {output:.2f}")
