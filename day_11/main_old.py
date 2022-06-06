"""
main.py
Created February 12, 2022 by Jennifer Baughman

Description: Text-based blackjack game
"""

from dataclasses import dataclass, field
from enum import Enum
from random import shuffle, choice


class Suit(Enum):
    HEART = "\u2665"
    CLUB = "\u2663"
    SPADE = "\u2660"
    DIAMOND = "\u2666"


class Rank(Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


@dataclass
class Card:
    suit: Suit
    rank: Rank
    _values = {"Ace": 0, "Two": 2, "Three": 3, "Four": 4, "Five": 5,
               "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
               "Jack": 10, "Queen": 10, "King": 10}
    
    @property
    def value(self):
        return self._values.get(self.rank)
    
    @property
    def name(self):
        return f"{self.rank} of {self.suit}"


def create_deck():
    # create deck
    deck = []
    
    for r in Rank:
        for s in Suit:
            deck.append(Card(s, r))
    return deck


def main():
    pass
    

if __name__ == '__main__':
    main()
