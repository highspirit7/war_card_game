from typing import Literal, List

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♥️", "♦️", "♣️", "♠️"]


class Card:
    def __init__(self, rank: str, suit: str):
        if rank in ranks and suit in suits:
            self._rank = rank
            self._suit = suit

    def __str__(self):
        return self.rank + self.suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


def compare_two_cards(
    user_card: Card, computer_card: Card
) -> Literal["user", "computer", "tie"]:
    if ranks.index(user_card.rank) > ranks.index(computer_card.rank):
        return "user"
    elif ranks.index(user_card.rank) < ranks.index(computer_card.rank):
        return "computer"
    else:
        return "tie"


def line_with_rank(card: Card, location: Literal["top", "bottom"]):
    if location == "top":
        return (
            "│{}        │".format(card.rank)
            if card.rank != "10"
            else "│{}       │".format(card.rank)
        )
    else:
        return (
            "│        {}│".format(card.rank)
            if card.rank != "10"
            else "│       {}│".format(card.rank)
        )


def ascii_of_two_cards(user_card: Card, computer_card: Card) -> None:
    lines = []
    lines.append("┌─────────┐" + "    " + "┌─────────┐")
    lines.append(
        line_with_rank(user_card, "top") + "    " + line_with_rank(computer_card, "top")
    )
    lines.append("│         │" + "    " + "│         │")
    lines.append("│         │" + "    " + "│         │")
    lines.append(
        "│    {}    │".format(user_card.suit)
        + "    "
        + "│    {}    │".format(computer_card.suit)
    )
    lines.append("│         │" + "    " + "│         │")
    lines.append("│         │" + "    " + "│         │")
    lines.append(
        line_with_rank(user_card, "bottom")
        + "    "
        + line_with_rank(computer_card, "bottom")
    )
    lines.append("└─────────┘" + "    " + "└─────────┘")

    for line in lines:
        print(line)


def ascii_of_cards_for_war(user_cards: List[Card], computer_cards: List[Card]) -> None:
    user_face_up_card = user_cards[-1]
    computer_face_up_card = computer_cards[-1]

    lines = []
    gap = "  |  "

    lines.append(
        "┌─────────┐ " * 3 + " ┌─────────┐" + gap + "┌─────────┐ " * 3 + " ┌─────────┐"
    )
    lines.append(
        "│░░░░░░░░░│ " * 3
        + " "
        + line_with_rank(user_face_up_card, "top")
        + gap
        + "│░░░░░░░░░│ " * 3
        + " "
        + line_with_rank(computer_face_up_card, "top")
    )
    lines.append(
        "│░░░░░░░░░│ " * 3 + " │         │" + gap + "│░░░░░░░░░│ " * 3 + " │         │"
    )
    lines.append(
        "│░░░░░░░░░│ " * 3 + " │         │" + gap + "│░░░░░░░░░│ " * 3 + " │         │"
    )
    lines.append(
        "│░░░░░░░░░│ " * 3
        + " │    {}    │".format(user_face_up_card.suit)
        + gap
        + "│░░░░░░░░░│ " * 3
        + " │    {}    │".format(computer_face_up_card.suit)
    )
    lines.append(
        "│░░░░░░░░░│ " * 3 + " │         │" + gap + "│░░░░░░░░░│ " * 3 + " │         │"
    )
    lines.append(
        "│░░░░░░░░░│ " * 3 + " │         │" + gap + "│░░░░░░░░░│ " * 3 + " │         │"
    )
    lines.append(
        "│░░░░░░░░░│ " * 3
        + " "
        + line_with_rank(user_face_up_card, "bottom")
        + gap
        + "│░░░░░░░░░│ " * 3
        + " "
        + line_with_rank(computer_face_up_card, "bottom")
    )
    lines.append(
        "└─────────┘ " * 3 + " └─────────┘" + gap + "└─────────┘ " * 3 + " └─────────┘"
    )
    for line in lines:
        print(line)


# This functions is for testing, not for end-user.
def print_cards(cards: List[Card], name: str) -> None:
    print(name)
    for card in cards:
        print(card, end=" ")
    print()
