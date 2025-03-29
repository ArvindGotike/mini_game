# Rock, Paper,Scissors with python

import random
import time
import os


def get_data(user_name):
    file_path = f"user_data/{user_name.lower()}_score.txt"

    if os.path.isfile(file_path):
        
        with open(file_path, "r") as user_file:
            file_data = user_file.read()
            if file_data != "":
                score = int(file_data)
            else:
                score = 0
    else:
        score = 0

    return score


def welcome_message(user_name, high_score):
    os.system('cls')
    print(f"\nHello {user_name},")
    print("Welcome to ROCK PAPER SCISSORS a fun and exciting game.")
    print(f"Your high score: {high_score:03d}")
    time.sleep(4)


def user_choice():
    os.system('cls')
    choices = {
        1: "  rock ",
        2: " paper ",
        3: "scissor"
        }
    print(
        "\nWinning rules of the game ROCK PAPER SCISSORS are:\n"
        "Rock vs Paper -> Paper wins \n"
        "Rock vs Scissors -> Rock wins \n"
        "Paper vs Scissors -> Scissors wins \n"
    )
    print(
       "\n********************"
       "\n* List of choices: *"
       "\n* 1 - Rock         *"
       "\n* 2 - Paper        *"
       "\n* 3 - Scissors     *"
       "\n********************"
    )

    while True:
        choice = input("\nEnter your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if choice in (1, 2, 3):
                break
            else:
                print("Use numbers 1, 2, 3 to select.")
                continue
        else:
            print("Please enter a number.")
            continue


    return choices[choice]


def computer_choice():
    choices = {
            1: "  rock ",
            2: " paper ",
            3: "scissor"
            }
    choice = random.choice([1, 2, 3])

    return choices[choice]
    

def decision():
    os.system('cls')
    user_move =  user_choice()
    computer_move = computer_choice()
    print(
        "\n*********************************"
        "\n* Your choice * Computer choice *"
        "\n*********************************"
        f"\n*   {user_move}     vs   {computer_move}    *"
        "\n*********************************"
    )

    if user_move == computer_move:
        return "draw"
    elif (
        (user_move == "  rock " and computer_move == "scissor")
        or (user_move == " paper " and computer_move == "  rock ")
        or (user_move == "scissor" and computer_move == " paper ")
    ):
        return "win"
    else:
        return "loose"


def result_output(result, high_score, score):
    if result == "win":
        print(
            "*       <== You won! ==>        *"
            "\n*********************************"
        )
        print(
            f"*      Current Score: {score:03d}       *"
            "\n*********************************"
            f"\n*        High Score: {high_score:03d}        *"
            "\n*********************************"
        )
    elif result == "loose":
        print(
            "*     <== Computer won! ==>     *"
            "\n*********************************"
        )
        print(
            f"*      Current Score: {score:03d}       *"
            "\n*********************************"
            f"\n*        High Score: {high_score:03d}        *"
            "\n*********************************"
        )
    else:
        print(
            "*      <== Its a draw! ==>      *"
            "\n*********************************"
        )
        print(
            f"*      Current Score: {score:03d}       *"
            "\n*********************************"
            f"\n*        High Score: {high_score:03d}        *"
            "\n*********************************"
        )


def update_score(high_score, user_name):
    file_path = f"user_data/{user_name.lower()}_score.txt"
    if not os.path.exists("user_data"):
        os.makedirs("user_data")

    with open(file_path, "w") as user_file:
        user_file.write(str(high_score))


def play_again(user_name):
    while True:
        play_again = input("Do you want to play again?( y/n )\n")
        if play_again in ("y", "n"):
            if play_again == "y":
                value = True
            elif play_again == "n":
                os.system('cls')
                print(
                    "\n*****************************************"
                    f"\n      Thankyou for playing {user_name}"
                    "\n*****************************************"
                )
                break
            return value
        else:
            print(
                "Invalid input.\nchoose ( y ) for ( yes ) and choose ( n ) for ( no )"
            )


def main():
    user_name = input("Enter your name: ")
    high_score = get_data(user_name)

    score = 0

    welcome_message(user_name, high_score)

    while True:
        result = decision()
        if result == "win":
            score += 1
        elif result == "loose":
            score = 0
        
        if score > high_score:
            high_score = score
            update_score(high_score, user_name)

        result_output(result, high_score, score)
        
        value = play_again(user_name)
        if value != True:
            break


if __name__ == '__main__':
    main()
