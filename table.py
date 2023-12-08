from typing import List
from utils import convert_to_ordinal
from card import Card


class Table:
    def __init__(self, user_cards: List[Card], computer_cards: List[Card]):
        self.war_count = 0
        self.user_cards = user_cards
        self.computer_cards = computer_cards
        self.cards = user_cards + computer_cards

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        self._cards = new_cards

    @property
    def user_cards(self):
        return self._user_cards

    @user_cards.setter
    def user_cards(self, new_cards):
        self._user_cards = new_cards

    @property
    def computer_cards(self):
        return self._computer_cards

    @computer_cards.setter
    def computer_cards(self, new_cards):
        self._computer_cards = new_cards

    def top_table_of_battle(self, round_num):
        ordinal_round_number = convert_to_ordinal(round_num)
        print(
            f"======================== Battle in {ordinal_round_number} round ========================"
        )

    def announce_war(self):
        pass

    def bottom_of_table(self):
        print("======================================================================")

    # def vizualize_table(self):
    #     if war:
    #         self.announce_war()
    #     else:
    #         self.top_table_of_battle()
    #     self.bottom_of_table()
    #     ...
    #     self.bottom_of_table()
