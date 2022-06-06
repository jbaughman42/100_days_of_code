"""
blackjack
Created February 13, 2022 by Jennifer Baughman

Description:

############### Blackjack Project #####################

Difficulty Normal 😎: Use all Hints below to complete the project.
Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
"""
from art import logo
from random import choice


def deal_cards(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(choice(cards))


def main():
    pass


if __name__ == '__main__':
    main()
