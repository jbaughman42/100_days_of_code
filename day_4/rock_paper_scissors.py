"""
rock_paper_scissors
Created January 31, 2022 by Jennifer Baughman

Description:
"""
from random import choice


def main():
    moves = ["rock", "paper", "scissors"]
    print("Let's play rock, paper, scissors!\n")
    player = input(
            "Are you rock, paper, or scissors ('rock', 'paper', 'scissors')? ")
    ai_choice = choice(moves)
    win = False
    if (player.lower() == 'rock' and ai_choice == 'scissors') or (
            player.lower() == 'scissors' and ai_choice == 'paper') or (
            player.lower() == 'paper' and ai_choice == 'rock'):
        win = True
    if win:
        print(f"{player.title()} beats {ai_choice.title()}!")
        print("Hooray, you win!")
    elif player.lower() == ai_choice:
        print(f"{ai_choice.title()} equals {player.title()}! ")
        print("It's a tie!")
    else:
        print(f"{ai_choice.title()} beats {player.title()}! ")
        print("Sorry, you lose!")


if __name__ == "__main__":
    main()
