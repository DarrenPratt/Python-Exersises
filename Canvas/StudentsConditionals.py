def calculate_grade():
    try:
        # Ask the student to input the number of correct answers
        correct_answers = int(input("Enter the number of questions you answered correctly (out of 70): "))
        
        # Total number of questions
        total_questions = 70

        # Calculate the percentage
        percentage = (correct_answers / total_questions) * 100

        # Determine the grade based on the percentage
        if percentage >= 80:
            grade = "Pass with distinction"
        elif 60 <= percentage < 80:
            grade = "Pass with merit"
        elif 50 <= percentage < 60:
            grade = "Pass"
        else:
            grade = "Fail"

        # Output the result
        print(f"You scored {percentage:.2f}% and your grade is: {grade}")

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid number of correct answers.")

# Call the function to execute the program
calculate_grade()
