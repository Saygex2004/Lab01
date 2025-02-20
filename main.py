# rock, paper, scissor

import random


def game():
    options = ["rock", "paper", "scissor"]

    while True:
        print("choose: rock, paper, scissor or exit to quit")
        while True:
            user_choice = input("Your choice: ")
            if user_choice == "exit":
                print("You left the game!")
                return
            if user_choice not in options:
                print("Invalid choice")
            else:
                break

        computer_choice = random.choice(options)
        print(f"Computer choice is:", computer_choice)

        if user_choice == computer_choice:
            print("Tie")

        elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissor"):
            print("User won")

        else:
            print("Computer won")
game()



# se scelta utente = sasso e computer = carta > WIN COMPUTER


# e via dicendo 