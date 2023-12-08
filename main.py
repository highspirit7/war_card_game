import random
from card import Card, compare_two_cards, ascii_of_two_cards, ascii_of_cards_for_war
from war_game import WarGame
from player import Player
from deck import Deck

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♥️", "♦️", "♣️", "♠️"]


def main():
    game = WarGame()
    game.print_guide_before_start()
    game.ask_user_to_play()
    deck = Deck()
    player_user_deck, player_computer_deck = deck.split_to_two_piles()
    player_user = Player(type="user", player_user_deck)
    computer_user = Player(type="computer", computer_computer_deck)
    ...


if __name__ == "__main__":
    main()
