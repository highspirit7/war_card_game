import random
from card import Card

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♥️", "♦️", "♣️", "♠️"]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def __str__(self):
        result = ""
        for card in self.cards:
            result += (card.rank + card.suit) + ", "
        return result[:-2]

    def shuffle(self):
        random.shuffle(self.cards)

    def split_to_two_piles(self):
        # getting midpoint 52/2=26 by floor division operator because we need integer, we can use "/" but it would give as a float number, and then we'd need to convert it to int.
        half = len(self.cards) // 2
        return self.cards[:half], self.cards[half:]
