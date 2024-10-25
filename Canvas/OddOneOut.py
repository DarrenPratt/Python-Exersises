# Python program for an odd-one-out game

def odd_one_out_game():
    # List of fruits and one vegetable as the odd one out
    items = ["apple", "banana", "orange", "potato"]

    # Correct answer
    correct_answer = "potato"

    # Print the question
    print("What is the odd one out: apple, banana, orange, potato.")

    # Ask the user for their answer and handle the case using lower() to match the list
    user_input = input("Enter the odd one out: ").lower()

    # Check if the user input matches the correct answer
    if user_input == correct_answer:
        print("Correct! Potato is the odd one out.")
    elif user_input in items:
        print("Incorrect! The odd one out is potato.")
    else:
        print("Invalid answer. Please choose one of the listed items.")

# Call the function to play the game
odd_one_out_game()
