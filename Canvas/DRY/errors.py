
'''
list = [23, "Car", 2.3, "Pen"]

for item in list
    print(item)

File "filepath\errors.py", line 3
    for item in list
                    ^
SyntaxError: expected ':'

     
'''

try:
    result = 10 / 5
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print (f"The answer is {result}.")
finally:
    print("End of program.")

'''
try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is not a valid age.")
else:
    print(f"You will be {age+5} in five years' time")
'''



while True:
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("That is not a valid age. ")
    else:
        print(f"You will be {age+5} in five years' time.")
        break


def calculate(num1, num2):
    """Performs addition on two numbers."""
    return num1 + num2

# Prompt the user for input with error handling
while True:
    try:
        # Ask the user for two values
        val1 = float(input("Enter the first number: "))
        val2 = float(input("Enter the second number: "))
        break  # Exit the loop if inputs are valid
    except ValueError:
        # Handle the error if inputs are not valid numbers
        print("Invalid input! Please enter numeric values.")

# Call the function with user inputs and display the result
result = calculate(val1, val2)
print(f"The result of adding {val1} and {val2} is: {result}")
