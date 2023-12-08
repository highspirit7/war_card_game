import random
from card import Card, compare_two_cards, ascii_of_two_cards, ascii_of_cards_for_war
from war_game import WarGame
from player import Player
from deck import Deck

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♥️", "♦️", "♣️", "♠️"]


def main():
    user_card = Card("10", "♠️")
    computer_card = Card("10", "♣️")
    user_war_cards = []
    computer_war_cards = []

    for _ in range(4):
        user_war_cards.append(Card(random.choice(ranks), random.choice(suits)))

    for _ in range(4):
        computer_war_cards.append(Card(random.choice(ranks), random.choice(suits)))

    # ascii_of_two_cards(user_card, computer_card)
    # ascii_of_cards_for_war(user_war_cards, computer_war_cards)


if __name__ == "__main__":
    main()
