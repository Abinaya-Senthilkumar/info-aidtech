import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def display_result(results):
    print("Result:",",".join(map(str, results)))

def main():
    print("Welcome to our Dice Rolling App!")

    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? (Enter 1 to 6): "))
            if num_dice >6:
                print("Please enter a number from 1 to 6")
                continue
            break
        except ValueError:
            print("Invalid input.Please enter a valid number")

    while True:
        results = roll_dice(num_dice)
        display_result(results)

        choice = input("Roll again? (yes/no): ").lower()

        if choice != 'yes':
            print("Thanks for using our App!")
            break

if __name__ == "__main__":
    main()
