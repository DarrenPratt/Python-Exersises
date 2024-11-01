import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Square root of a negative number is not allowed."

def power(x, y):
    return math.pow(x, y)

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power (x^y)")
        print("7. Exit")

        try:
            choice = int(input("Choose an operation (1-7): "))

            if choice == 7:
                print("Exiting the calculator. Goodbye!")
                break
            elif choice in [1, 2, 3, 4, 6]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    result = addition(num1, num2)
                    print(f"The result of addition is: {result}")
                elif choice == 2:
                    result = subtraction(num1, num2)
                    print(f"The result of subtraction is: {result}")
                elif choice == 3:
                    result = multiplication(num1, num2)
                    print(f"The result of multiplication is: {result}")
                elif choice == 4:
                    result = division(num1, num2)
                    print(f"The result of division is: {result}")
                elif choice == 6:
                    result = power(num1, num2)
                    print(f"The result of {num1} raised to the power of {num2} is: {result}")

            elif choice == 5:
                num = float(input("Enter the number to find the square root: "))
                result = square_root(num)
                print(f"The square root of {num} is: {result}")

            else:
                print("Invalid choice. Please select a number between 1 and 7.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the calculator
calculator()
