from typing import Literal, Union
import sys
from player import Player
from deck import Deck
from utils import convert_to_ordinal


class WarGame:
    def __init__(self, user: Player, computer: Player, deck: Deck) -> None:
        self.round = 0
        self.is_game_over = False
        self.user = user
        self.computer = computer
        self.deck = deck

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, number):
        if type(number) != "int":
            raise TypeError("WarGame round type must be integer")

        if number < 0:
            raise ValueError("WarGame round value must be positive integer or 0")

        self._round = number

    @property
    def is_game_over(self):
        return self._is_game_over

    @is_game_over.setter
    def is_game_over(self, value):
        if type(value) != "bool":
            raise TypeError("WarGame is_game_over must be boolean")

        self._is_game_over = value

    def ask_user_to_play(self, round: int) -> None:
        user_input
        if round:
            user_input = input(
                "Do you want to continue playing into the next round?(yes/no): "
            )
        else:
            user_input = input("Do you want to start war game?(yes/no): ")
        if user_input.lower()[0] == "n":
            self.exit_war_game()

    def announce_winner_of_round(
        player: Literal["user", "computer"], round: int
    ) -> None:
        winner = "You" if player == "user" else "Computer"
        print(
            "\n"
            + f"{winner} has won in the {convert_to_ordinal(round)} round. So {winner} takes all the card on the table."
            + "\n"
        )

    def announce_winner_of_game(
        player: Literal["user", "computer"], round: int
    ) -> None:
        winner = "You" if player == "user" else "Computer"
        print(
            "\n"
            + f"{round} rounds were held in total. and {winner} has won this war game!!"
        )

    def show_cards_of_players(user: Player, computer: Player) -> None:
        print(
            f"====== Currently {user.type} has {len(user.card_pile)} card // {computer.type} has {len(computer.card_pile)} ======"
            + "\n"
        )

    def get_winner_of_game(
        user_cards, computer_cards
    ) -> Union[Literal["user", "computer"], None]:
        if not len(user_cards):
            return "computer"
        elif not len(computer_cards):
            return "user"
        else:
            return

    def exit_war_game() -> None:
        sys.exit(
            """
  _____                   ____                 
 / ___/___ _ __ _  ___   / __ \ _  __ ___  ____
/ (_ // _ `//  ' \/ -_) / /_/ /| |/ // -_)/ __/
\___/ \_,_//_/_/_/\__/  \____/ |___/ \__//_/   
                                               
"""
        )

    def print_guide_before_start() -> None:
        print(
            """
    [PLAY GUIDE]
    War(card game) is a fun card game where players try to win all of the cards in the deck.
    This game uses one standard deck of playing cards.(the version of this war game does not use joker cards, 
    so the total number of cards for this game is 52.)
    Once you play this game, you will play against computer.
    Your card will be located on the left side and
    computer's card will be located on the right side on the table.

    """
        )

    
