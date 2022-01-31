"""
day_three_choose_your_own_adventure
Created January 29, 2022 by Jennifer Baughman

Description: Create a small choose your own adventure game!

Note: this is done in Python 3.9 so does not include switch statement
"""
import sys


def adventure():
    cmd = input(
            "You have come to a crossroads. Which way would you like to go? "
            "Type "
            "'left' or 'right'\n")
    if cmd.upper() != "LEFT":
        print("It is dark. You have been eaten by a grue.\n***GAME OVER***")
        sys.exit()
    cmd = input(
            "You wander down the road, eventually coming to a lake. There is "
            "an island in the middle of the lake. How do you want to get "
            "across?\nType 'wait' to wait for a boat. Type 'swim' to swim "
            "across.\n")
    if cmd.upper() != "WAIT":
        print(
                "OH NO! This lake is full of hungry piranhas! You scream and "
                "flail as your flesh is savaged from your bones, and your "
                "defleshed skeleton sinks to the bottom of the "
                "waters!\n***GAME OVER***")
        sys.exit()
    cmd = input(
            "You arrive at the island unharmed. Before you is a house with "
            "three doors: one red, one yellow, and one blue. Which door do "
            "you choose?\n")
    if cmd.upper() == "RED":
        print(
                "The room you're in bursts into flames all around you! Before "
                "you can turn to run, the flames envelope you! All that "
                "remains is ash...\n***GAME OVER***")
        sys.exit()
    elif cmd.upper() == "YELLOW":
        print(
                "You open the door to find a pit of starving beasts! They're "
                "on you before you realize it, and the last thing you feel is "
                "jaws clamping on your throat!\n***GAME OVER***")
        sys.exit()
    elif cmd.upper() == "BLUE":
        print(
                "Before you sits a giant chest, overflowing with treasure! "
                "This must be the fabled treasure of Treasure "
                "Island!\n***GAME OVER***")
        sys.exit()
    else:
        print(
                "You turn around, but suddenly everything disappears in a "
                "waterfall of digital data. You're trapped in the Matrix, "
                "and you're never going to escape.\n***GAME OVER***")
        sys.exit()


def main():
    print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
    adventure()


if __name__ == '__main__':
    main()
