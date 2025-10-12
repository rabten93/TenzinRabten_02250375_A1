def guess_number_game():
    """Play a number guessing game between 1 and 100."""
    number = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100...")

    while True:
        guess = input("Guess the number: ")
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def rock_paper_scissors_game():
    """Play Rock Paper Scissors against the computer."""
    choices = ["rock", "paper", "scissors"]
    wins = 0
    losses = 0
    ties = 0

    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print(f"Final Score → Wins: {wins}, Losses: {losses}, Ties: {ties}")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

def main():
    while True:
        print("\nSelect a game (1-3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit program")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()