from datetime import datetime

def greet_and_calculate_birth_year():
    # Get the current year
    current_year = datetime.now().year

    # Get user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate birth year
    birth_year = current_year - age

    # Greet the user and tell them their birth year
    print(f"Hello, {name}! You were born in {birth_year}.")

# Run the function
greet_and_calculate_birth_year()
