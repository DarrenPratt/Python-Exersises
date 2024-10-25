def convert_temperature():
    try:
        # Ask the user which conversion they want to perform
        choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

        if choice == 'C':
            # Convert Celsius to Fahrenheit
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        
        elif choice == 'F':
            # Convert Fahrenheit to Celsius
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) / 1.8
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        
        else:
            print("Invalid choice. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle the case where input is not a valid number
        print("Invalid input. Please enter a valid number.")

# Call the function to execute the program
convert_temperature()
