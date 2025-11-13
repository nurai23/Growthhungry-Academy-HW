import random

def play_guessing_game():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    guessed_correctly = False

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print("Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Invalid input. Please enter an integer.")

play_guessing_game()