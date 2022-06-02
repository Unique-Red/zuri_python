import random

while True:
    user_choice = input("Enter a choice ('R' for 'rock', 'P' for 'paper','S' for 'scissors'): ")
    available_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(available_options)
    print(f"\nYou chose {user_choice}, CPU chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock" or "R":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper" or "P":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors" or "S":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    repeat = input("Play again? (y/n): ")
    if repeat.lower() != "y":
        break
