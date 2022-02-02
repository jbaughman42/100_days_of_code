"""
hangman
Created February 01, 2022 by Jennifer Baughman

Description:
"""

from random import choice
from hangman_art import stages, logo
from hangman_words import word_list


def main():
    print(logo)
    word = choice(word_list)
    word_length = len(word)
    display = ['_' for _ in range(word_length)]
    print(''.join(display))
    lives = 6
    end_of_game = False
    guesses = []
    while not end_of_game:
        # Get letter input and convert to lower for consistency
        guess = input("Guess a letter: ").lower()
        
        # check to see if letter is already guessed
        # could go vs. display but this catches failed guesses too
        if guess in guesses:
            print(f"You've already guessed the letter {guess}!")
            continue
        
        # track guessed letters
        guesses.append(guess)
        
        # if not in the word, lose a life and print output
        if guess not in word:
            lives -= 1
            print(f"The letter {guess} is not in the word!")
            print(f"You lose a life! Lives left: {lives}")
            print(stages[lives])
        
        # if in the word, update the display with the positions of the letters
        else:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = letter
        
        print(''.join(display))
        
        # win/lose condition check
        if lives == 0:
            print("YOU LOSE!")
            print(f"The word was {word}!")
            end_of_game = True
        
        if '_' not in display:
            print("You Win!")
            end_of_game = True


if __name__ == "__main__":
    main()
