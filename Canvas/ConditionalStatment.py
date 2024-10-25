def check_conditions(age, score):
    # Use logical operators to check two conditions
    if age >= 18 and score >= 20:
        print("You are eligible and you passed the test.")

        # Nested conditional to further check the score
        if score >= 25:
            print("Excellent performance! You scored above 25.")
        else:
            print("Good job, but you can improve!")
    else:
        print("You are either too young or did not pass the test.")

check_conditions(18, 22)