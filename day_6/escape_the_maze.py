"""
escape_the_maze
Created February 01, 2022 by Jennifer Baughman

Description: Works in concert with Reeborg's World
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus
%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""


def turn_right():
    for i in range(3):
        turn_left()


while front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
