import random

def print_welcome_message():
    print("Welcome to the Guessing Game!")
    print("You will have to guess the number that was generated using subtle hints!")
    print("Type 'exit' to quit at any time.")

def print_exit_message():
    print("Thanks for playing! Goodbye!")

def get_level_choice():
    while True:
        level = input("Please choose a level (1 for 1-100, 2 for 1-1000): ")
        if level == '1':
            return 100
        elif level == '2':
            return 1000
        elif level.lower() == 'exit':
            return None
        else:
            print("Invalid input. Please enter '1', '2', or 'exit'.")

def play_round(max_number):
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess_input = input(f"Please enter your guess (1-{max_number}) or type 'exit' to quit: ")
        
        if guess_input.lower() == 'exit':
            return False

        try:
            guess = int(guess_input)
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                return True

        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")

    print(f"You've reached the maximum of {max_attempts} attempts. The game is over.")
    print(f"The number was {number_to_guess}.")
    return True

def play_guessing_game():
    print_welcome_message()

    while True:
        choice = input("Do you want to play? (yes/no): ")
        if choice.lower() != "yes":
            break

        max_number = get_level_choice()
        if max_number is None:
            break
        
        print("Great! Let's start!")
        
        if not play_round(max_number):
            break

        play_again_choice = input("Would you like to play another round? (yes/no): ")
        if play_again_choice.lower() != 'yes':
            break
            
    print_exit_message()