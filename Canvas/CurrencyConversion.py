def currency_converter():
    '''
    # Conversion rates (you may need to update them with actual rates)
    conversion_rate_to_usd = 1.37  # Example rate from GBP to USD
    conversion_rate_to_gbp = 0.73  # Example rate from USD to GBP

    while True:
        try:
            # Ask the user for the amount to convert
            amount = float(input("Enter the amount to convert: "))

            # Ask the user for the target currency (either USD or GBP)
            target_currency = input("Enter the target currency (USD or GBP): ").upper()

            # Convert the amount based on the target currency
            if target_currency == "USD":
                converted_amount = amount * conversion_rate_to_usd
                print(f"{amount} GBP is equal to {converted_amount:.2f} USD.")
            elif target_currency == "GBP":
                converted_amount = amount * conversion_rate_to_gbp
                print(f"{amount} USD is equal to {converted_amount:.2f} GBP.")
            else:
                print("Invalid currency. Please enter either 'USD' or 'GBP'.")

            # Ask the user if they want to convert another amount
            repeat = input("Do you want to convert another amount? (yes/no): ").lower()
            if repeat != "yes":
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function to run the currency converter
currency_converter()
'''

# Define the conversion factors dictionary globally so it can be accessed by both functions
conversion_factors = {    
    "USD": {"GBP": 0.71, "EUR": 0.83, "JPY": 109.23},   
    "GBP": {"USD": 1.41, "EUR": 1.17, "JPY": 151.57},    
    "EUR": {"USD": 1.21, "GBP": 0.85, "JPY": 130.59},    
    "JPY": {"USD": 0.0092, "GBP": 0.0066, "EUR": 0.0076}
}

def convert_currency(amount, source_currency, target_currency):
    # Convert the amount to the target currency using the conversion factor
    converted_amount = amount * conversion_factors[source_currency][target_currency]
    return converted_amount

def multi_currency_converter():
    while True:
        try:
            # Ask the user for the amount to convert
            amount = float(input("Enter the amount to convert: "))

            # Ask the user for the source currency and target currency
            source_currency = input("Enter the source currency (USD, GBP, EUR, JPY): ").upper()
            target_currency = input("Enter the target currency (USD, GBP, EUR, JPY): ").upper()

            # Ensure valid source and target currencies
            if source_currency in conversion_factors and target_currency in conversion_factors[source_currency]:
                # Convert the amount
                converted_amount = convert_currency(amount, source_currency, target_currency)
                print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
            else:
                print("Invalid currency code. Please enter valid source and target currencies.")

            # Ask the user if they want to convert another amount
            repeat = input("Do you want to convert another amount? (yes/no): ").lower()
            if repeat != "yes":
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function to run the multi-currency converter
multi_currency_converter()
