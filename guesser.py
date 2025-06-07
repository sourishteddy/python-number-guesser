import random

def playing_guessing_game():
    print("Welcome to the Guessing Game!")
    print("You will have to guess the number that was generated using subtle hints!")
    print("Type 'exit' to quit at any time.")

while True:
    choice = input("Do you want to play? (yes/no): ")
    if choice.lower() != "yes":
        if choice.lower() == 'no':
            print("Alright, maybe next time! Goodbye!")
        elif choice.lower() == 'exit':
             print("Thanks for playing! Goodbye!")
        break

    max_number = 0
    while True:
        level = input("Please choose a level (1 for 1-100, 2 for 1-1000): ")
        if level == '1':
            max_number = 100
            break
        elif level == '2':
            max_number = 1000
            break
        elif level.lower() == 'exit':
            break
        else:
            print("Invalid input. Please enter '1' or '2'.")
    
    if max_number == 0:
        print("Thanks for playing! Goodbye!")
        break

    print("Great! Let's start!")
    number = random.randint(1, max_number)
    attempts = 0

    while True:
        guess = input(f"Please enter your guess (1-{max_number}) or type 'exit' to quit: ")
        if guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        try:
            guess = int(guess)
            attempts += 1
            if attempts >= 10:
                print("You've reached the maximum number of attempts. The game is over.")
                print(f"The number was {number}.")
                break

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
                break 
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")
    
    if guess.lower() == 'exit':
        break

    play_again_choice = input("Would you like to play another round? (yes/no): ")
    if play_again_choice.lower() != 'yes':
        print("Thanks for playing! Goodbye!")
        break