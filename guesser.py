import random

def playing_guessing_game():
    print("Welcome to the Guessing Game!")
    print("You will have to guess the number that was generated using subtle hints!")
    print("Type 'exit' to quit at any time.")
choice = input("Do you want to play? (yes/no): ")
if choice == "yes":
    print("Great! Let's start!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Please enter your guess (or type 'exit' to quit): ")
        if guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        try:
            guess = int(guess)
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                choice = input(f"Congratulations! You've guessed the number {number} in {attempts} attempts! Would you like to play again? (yes/no): ")
                if choice == 'yes':
                    number = random.randint(1, 100)
                    attempts = 0
                    
                else:
                    print("Thanks for playing! Goodbye!")
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")