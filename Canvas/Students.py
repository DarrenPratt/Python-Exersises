def check_pass_or_fail():
    try:
        # Ask the student to input their score
        score = int(input("Enter your score (out of 30): "))

        # Define the passing criteria
        passing_score = 20

        # Check if the student passed or failed
        if score >= passing_score:
            print(f"Congratulations! You passed with a score of {score}.")
        else:
            print(f"Sorry, you failed. You scored {score}. You needed at least 20 to pass.")
    
    except ValueError:
        # Handle the case where input is not a valid number
        print("Invalid input. Please enter a valid score as an integer.")

# Call the function to execute the program
check_pass_or_fail()
