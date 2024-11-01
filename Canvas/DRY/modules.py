import math
number = float(input("Enter a number: "))
answer = math.sqrt(number)
print(answer)



'''
https://docs.python.org/3/library/
print(dir(math))
'''


# Importing multiple modules

from math import pi, ceil
from random import randint

def random_pi():
    return ceil(randint(1, 10) * pi)

for _ in range(5):
    print(random_pi())


import math

# Define a function that uses sin, cos, and radians from the math module
def trigonometry_operations(angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert degrees to radians
    sine_value = math.sin(angle_radians)         # Calculate sine of the angle
    cosine_value = math.cos(angle_radians)       # Calculate cosine of the angle
    
    return angle_radians, sine_value, cosine_value

# Ask the user for an angle in degrees
try:
    angle = float(input("Enter an angle in degrees: "))

    # Call the function with the user input and display the results
    radians, sin_val, cos_val = trigonometry_operations(angle)
    print(f"The angle {angle} degrees in radians is: {radians}")
    print(f"The sine of {angle} degrees is: {sin_val}")
    print(f"The cosine of {angle} degrees is: {cos_val}")

except ValueError:
    print("Invalid input! Please enter a numeric value for the angle.")
