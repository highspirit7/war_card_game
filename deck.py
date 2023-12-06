import random, Card
class Deck:
    def __init__(self):
        suits = ["♥️", "♦️", "♣️", "♠️"]  
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self):
        half = len(self.cards) // 2 # getting midpoint 52/2=26 by floor division operator because we need integer, we can use "/" but it would give as a float number, and then we'd need to convert it to int.
        return self.cards[:half], self.cards[half:]