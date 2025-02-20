# rock, paper, scissor

import random
import csv
from idlelib.iomenu import encoding


def game():
    options = ["rock", "paper", "scissor"]

    nickname = input("Insert your nickname:")
    print(f"Welcome {nickname}")

    games_play = 0
    user_win = 0
    user_lose = 0
    counter_tie = 0

    while True:
        print("choose: rock, paper, scissor or exit to quit")
        while True:
            user_choice = input("Your choice: ")
            if user_choice == "exit":
                print("You left the game!")
                with open("tabella.csv",mode= 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    #writer.writerow(["Nickname","Games_play","Win","Loss","Tie"])
                    writer.writerow([nickname,games_play,user_win,user_lose,counter_tie])

                return
            if user_choice not in options:
                print("Invalid choice")
            else:
                break

        computer_choice = random.choice(options)
        print(f"Computer choice is:", computer_choice)
        games_play +=1

        if user_choice == computer_choice:
            print("Tie")
            counter_tie +=1

        elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissor"):
            print("User won")
            user_win +=1

        else:
            print("User lose")
            user_lose +=1

        print(f"games_play:{games_play} \n user_win:{user_win} \n user_lose: {user_lose} \n tie: {counter_tie} ")
game()


