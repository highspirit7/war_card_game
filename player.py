from typing import Literal, List
from card import Card


class Player:
    def __init__(self, type: Literal["user", "computer"], cards: List[Card]):
        self.type = type
        self.card_pile = cards

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: Literal["user", "computer"]):
        if value != "computer" and value != "user":
            raise ValueError("Player type must be 'user' or 'computer'")
        self._type = value

    @property
    def card_pile(self):
        return self._card_pile

    @card_pile.setter
    def card_pile(self, cards: List[Card]):
        if len(cards) != 26:
            raise
        self._card_pile = cards

    def flip_top_card(self) -> Card:
        return self.card_pile.pop()

    def cards_for_war(self) -> List[Card]:
        return self.card_pile[-4:]

    def win_cards(self, cards):
        self.card_pile.extend(cards)