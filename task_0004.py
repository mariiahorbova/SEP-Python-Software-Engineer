# 4. Write a Python program which accepts the radius of a circle from the user and compute the parameter and area.
# Sample Output:
# Input the radius of the circle: The perimeter is 31.41592653.
# The area is 78.539816325.
from math import pi


def circle_param_and_area():
    r = int(input("Input the radius of the circle:"))
    perimeter = pi * r ** 2
    area = 2 * pi * r
    # I did round to 6 digits, but can be more
    print("The perimeter is", round(perimeter, 6))
    print("The area is", round(area, 6))


circle_param_and_area()
