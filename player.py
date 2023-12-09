from typing import Literal, List
from card import Card
import random
from constants import colors


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
        self._card_pile = cards

    def flip_top_card(self) -> Card:
        return self.card_pile.pop()

    def flip_cards_for_war(self) -> List[Card]:
        cards_for_war = []
        for _ in range(4):
            cards_for_war.append(self.card_pile.pop())
        return cards_for_war

    def win_cards(self, cards):
        random.shuffle(cards)
        self.card_pile = cards + self.card_pile


def show_cards_of_players(user: Player, computer: Player) -> None:
    print(
        f"{colors['yellow']}\n====== Currently the number of your cards is {len(user.card_pile)} // {computer.type} has {len(computer.card_pile)} ======{colors['end']}"
        + "\n"
    )
