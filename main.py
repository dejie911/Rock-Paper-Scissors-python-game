import random

#R for Rock, P for paper and S for scissors
while True:
    user_option = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_option}, computer chose {computer_action}.\n")
    if user_option == computer_action:
        print(f"Both players selected {user_option}. It's a tie!")
    elif user_option == "R":
        if computer_action == "scissors":
            print("R smashes S! You win!")
        else:
            print("P covers R! You lose.")
    elif user_option == "P":
        if computer_action == "rock":
            print("P covers R! You win!")
        else:
            print("S cuts P! You lose.")
    elif user_option == "S":
        if computer_action == "P":
            print("S cuts P! You win!")
        else:
            print("R smashes S! You lose.")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

