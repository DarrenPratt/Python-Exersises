def calculate_future_age():
    try:
        # Ask the user for their age
        age = int(input("Enter your age: "))

        # Use an f-string to print the age in 5 years
        print(f"You will be {age + 5} years old in five years' time.")
    
    except ValueError:
        # Handle the case where input is not an integer
        print("Invalid input. Please enter a valid age.")

# Call the function to execute the program
calculate_future_age()
