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

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Choose an operation (1-5): "))

            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break
            elif choice in [1, 2, 3, 4]:
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
            else:
                print("Invalid choice. Please select a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the calculator
calculator()
