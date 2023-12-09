from typing import Literal, Union, List
from card import Card
import sys, time
from utils import convert_to_ordinal
from constants import styles, colors


class WarGame:
    def __init__(self) -> None:
        self.round = 0
        self.is_game_over = False

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, number):
        if type(number) != int:
            raise TypeError("WarGame round type must be integer")

        if number < 0:
            raise ValueError("WarGame round value must be positive integer or 0")

        self._round = number

    @property
    def is_game_over(self):
        return self._is_game_over

    @is_game_over.setter
    def is_game_over(self, value):
        if type(value) != bool:
            raise TypeError("WarGame is_game_over must be boolean")

        self._is_game_over = value

    def ask_user_to_play(self, round: int) -> None:
        user_input = ""

        if round:
            user_input = input(
                "Do you want to continue playing into the next round?(yes/no): "
            )
        else:
            user_input = input("Do you want to start war game?(yes/no): ")
        print()
        if user_input.lower()[0] == "n":
            self.is_game_over = True
            self.exit_war_game()

    def announce_winner_of_round(self, player: Literal["user", "computer"]) -> None:
        winner = "You" if player == "user" else "Computer"
        print(
            f"{winner} has won in the {convert_to_ordinal(self.round)} round. So {winner.lower()} takes all the card on the table."
            + "\n"
        )

    def announce_winner_of_game(
        self, result: Literal["user", "computer", "tie"]
    ) -> None:
        if result != "tie":
            winner = "You" if result == "user" else "Computer"
            print(
                "\n"
                + f"{styles['bold']}{self.round} rounds were held in total. and {winner} has won this war game!!{styles['reset']}"
            )
        else:
            print(
                "\n"
                + f"{styles['bold']}Both of players do not have enough cards for war!!! This game ends in a tie...{styles['reset']}"
            )

    def announce_war(self) -> None:
        print()

        for i in [".", ".", ".", " going to War!!!"]:
            sys.stdout.write(str(i) + " ")
            sys.stdout.flush()
            time.sleep(0.5)

    def exit_war_game(self) -> None:
        sys.exit(
            f"""{colors['green']}
  _____                   ____                 
 / ___/___ _ __ _  ___   / __ \ _  __ ___  ____
/ (_ // _ `//  ' \/ -_) / /_/ /| |/ // -_)/ __/
\___/ \_,_//_/_/_/\__/  \____/ |___/ \__//_/   
                                               
"""
        )

    def print_guide_before_start(self) -> None:
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


def check_cards_before_war(
    user_cards: List[Card], computer_cards: List[Card]
) -> Literal["tie", "user", "computer", "continue"]:
    if len(user_cards) < 4 and len(computer_cards) < 4:
        return "tie"
    if len(user_cards) < 4:
        print(
            f"{colors['red']}\n!!!User does not have enough cards for war!!!{colors['end']}"
        )
        return "computer"
    if len(computer_cards) < 4:
        print(
            f"{colors['red']}\n!!!Computer does not have enough cards for war!!!{colors['end']}"
        )
        return "user"

    return "continue"


def get_winner_of_game(
    user_cards, computer_cards
) -> Union[Literal["user", "computer"], None]:
    if not len(user_cards):
        return "computer"
    elif not len(computer_cards):
        return "user"
    else:
        return
