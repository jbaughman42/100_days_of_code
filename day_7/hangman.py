"""
hangman
Created February 01, 2022 by Jennifer Baughman

Description:
"""

from random import choice

STAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

WORD_LIST = ["aardvark", "baboon", "camel"]


def main():
    end_of_game = False
    word = choice(WORD_LIST)
    word_length = len(word)
    display = ['_' for _ in range(word_length)]
    print(''.join(display))
    lives = 6
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        guess_used = False
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = letter
                guess_used = True
        if not guess_used:
            lives -= 1
        print(STAGES[lives])
        print(''.join(display))
        if lives == 0:
            print("YOU LOSE!")
            end_of_game = True
        if '_' not in display:
            print("You Win!")
            end_of_game = True
            


if __name__ == "__main__":
    main()
