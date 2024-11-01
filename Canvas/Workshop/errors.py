#Code example one:
def name(name, age):

       return name + age

print(name("Victoria", 29))

'''
Error: This will cause a TypeError.
Reason: Python cannot concatenate a string ("Victoria") with an integer (29). The + operator requires both operands to be of the same type (both strings or both integers).
'''


# Code example two:
import math

def square(x):

      return math.sqrt(x)

print(square(-10))

'''Error: This will cause a ValueError.
Reason: The math.sqrt function does not accept negative numbers, as the square root of a negative number is undefined in the real number domain.
 Passing -10 results in a "math domain error".
 '''

# Code example three:
def function(x, y):

    return x * y

print(function("20", "40"))

'''
No Error: This code will execute successfully.
Reason: Multiplying two strings together would cause an error,
but here, one string ("20") is multiplied by another string ("40"). The operation is syntactically correct in Python and will concatenate "20" forty times.
'''


# Code example four:
import math

def square(x):

      return math.sqrt(x)

print(square("10"))

'''Error: This will cause a TypeError.
Reason: The math.sqrt function expects a numeric argument (an integer or a float), but "10" is a string. Passing a string to math.sqrt will result in a type mismatch.
'''

# Code example five:
def function(name: str):

      return name

text = int(input("Please enter a name: "))

print(function(text))

'''Error: This will cause a ValueError if the user enters non-numeric input.
Reason: The int conversion attempts to interpret user input as an integer.
If the input is not a number (e.g., a name like "Victoria"), Python will raise a ValueError since it cannot convert non-numeric text to an integer.
'''


'''
Summary of Errors:
Code Example One: TypeError
Code Example Two: ValueError
Code Example Three: No Error
Code Example Four: TypeError
Code Example Five: ValueError if non-numeric input is provided.
'''