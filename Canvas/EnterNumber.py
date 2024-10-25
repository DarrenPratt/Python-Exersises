def add_five():
    try:
        # Ask the user for a number
        user_input = int(input("Enter a number: "))
        
        # Add 5 to the number
        result = user_input + 5

        # Print the result
        print(f"Your number plus 5 is: {result}")
    
    except ValueError:
        # Handle the case where input is not an integer
        print("Invalid input. Please enter an integer.")

# Call the function to execute the program
add_five()
