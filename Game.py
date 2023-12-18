import random

# Define function to get the user's choice of rock, paper, or scissors
def get_user_choice():
    while True:
        user_choice = input("r = rock \np = paper \ns = scissors \nEnter your choice: ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# Define function for computer to randomly choose
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Define function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'r' and computer_choice == 'scissors') or
            (user_choice == 'p' and computer_choice == 'rock') or
            (user_choice == 's' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "You lose!"

# Define main function to play the game
def play_game():
    print("\nWelcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# run the progam if name is main
if __name__ == "__main__":
    play_game()