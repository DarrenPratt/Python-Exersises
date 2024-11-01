# TypeError Example with Exception Handling

def name(name, age):
    try:
        return name + age
    except TypeError:
        return "Error: Cannot concatenate a string and an integer. Please ensure both are of the same type."

# Testing the function
print(name("Victoria", 29))  # This will trigger the TypeError


import math

# ValueError Example with Exception Handling

def square(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error: Cannot calculate the square root of a negative number."

# Testing the function
print(square(-10))  # This will trigger the ValueError




# TypeError Example with Exception Handling

def name(name, age):
    try:
        return name + age
    except TypeError:
        return "Error: Cannot concatenate a string and an integer. Please ensure both are of the same type."

# Testing the function
print(name("Victoria", 29))  # This will trigger the TypeError


import math

# ValueError Example with Exception Handling

def square(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error: Cannot calculate the square root of a negative number."

# Testing the function
print(square(-10))  # This will trigger the ValueError


# No Error Example, but Adding Exception Handling for Unexpected Errors

def function(x, y):
    try:
        return x * y
    except TypeError:
        return "Error: Multiplication operation requires compatible data types."

# Testing the function
print(function("20", "40"))  # This will successfully repeat "20" forty times

import math

# TypeError Example with Exception Handling

def square(x):
    try:
        return math.sqrt(x)
    except TypeError:
        return "Error: Input must be a numeric value for square root calculation."

# Testing the function
print(square("10"))  # This will trigger the TypeError

# ValueError Example with Exception Handling for Input Conversion

def function(name: str):
    return name

try:
    # Attempt to convert user input to an integer
    text = int(input("Please enter a name: "))
    print(function(text))
except ValueError:
    print("Error: Invalid input. Please enter a valid name as text, not a number.")
