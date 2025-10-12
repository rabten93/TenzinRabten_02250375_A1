import random  # For generating random numbers and choices

# This is the "Guess the Number" game
def guess_number_game():
    print("\nI'm thinking of a number between 1 and 100...")
    number_to_guess = random.randint(1, 100)  # Random number to guess
    attempts = 0  # Track number of tries

    while True:
        guess_input = input("Take a guess: ")

        if not guess_input.isdigit():
            print("That's not a valid number. Please enter a number between 1 and 100.")
            continue

        guess = int(guess_input)

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try a higher number.")
        elif guess > number_to_guess:
            print("Too high. Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.\n")
            break

# This is the "Rock, Paper, Scissors" game
def rock_paper_scissors_game():
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    computer_wins = 0
    rounds = 0

    print("\nWelcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to go back): ").lower()

        if user_choice == 'quit':
            print(f"\nFinal Score: You {user_wins} - Computer {computer_wins} (Rounds played: {rounds})\n")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie.")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_wins += 1
        else:
            print("You lose this round.")
            computer_wins += 1

        rounds += 1
        print(f"Current Score: You {user_wins} | Computer {computer_wins}\n")

# This is the main menu
def main():
    print("🎮 Welcome to the Game Zone!")

    while True:
        print("\nPlease choose a game:")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    main()
