import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("Let's see if you can guess the correct number.")
    print("But first, I'd like to know your name.")

def get_player_name():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Are you ready to play?")

def explain_rules():
    print("Here are the rules:")
    print("1. I will randomly choose a number between 1 and 100.")
    print("2. You have to guess the correct number within 10 attempts.")
    print("3. After each guess, I'll tell you if your guess is too high or too low.")
    print("4. If you guess the correct number, you win! Otherwise, the game ends.")
    print("Let's get started!")
    

def play_game():
    random_number = random.randint(1, 100)
    attempts_left = 10

    while attempts_left > 0:
        user_guess = int(input("Enter your guess: "))

        if user_guess == random_number:
            print(f"Congratulations! You guessed the correct number, {random_number}! You win!")
            break
        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts_left -= 1
        print(f"Attempts left: {attempts_left}\n")

    if attempts_left == 0:
        print(f"Sorry,you've run out of attempts.The correct number was {random_number}.The Game is over.")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    welcome_message()
    get_player_name()
    explain_rules()
    

    while True:
        play_game()

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
