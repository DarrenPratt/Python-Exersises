import random
number_to_guess = random.randint(1, 20)
guess = None
while guess != number_to_guess:
    guess = int(input('Guess the number between 1 and 20: '))
    if guess < number_to_guess:
        print('Too low!')
    elif guess > number_to_guess:
        print('Too high!')
    else:
        print('Congratulations! You guessed it.')
