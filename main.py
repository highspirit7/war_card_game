from table import Table
from card import Card, compare_two_cards, ascii_of_two_cards, ascii_of_cards_for_war
from war_game import WarGame
from player import Player, show_cards_of_players
from deck import Deck

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♥️", "♦️", "♣️", "♠️"]


def main():
    game = WarGame()
    game.print_guide_before_start()
    game.ask_user_to_play(game.round)
    deck = Deck()
    player_user_deck, player_computer_deck = deck.split_to_two_piles()
    user = Player(type="user", cards=player_user_deck)
    computer = Player(type="computer", cards=player_computer_deck)

    while not game.is_game_over:
        game.round += 1

        user_top_card = user.flip_top_card()
        computer_top_card = computer.flip_top_card()

        # for card in user.card_pile:
        #     print(card, end=" ")
        # print()
        # for card in computer.card_pile:
        #     print(card, end=" ")
        # print()

        game_table = Table([user_top_card], [computer_top_card])
        game_table.top_table_of_battle(game.round)
        ascii_of_two_cards(user_top_card, computer_top_card)
        game_table.bottom_of_table()

        battle_result = compare_two_cards(user_top_card, computer_top_card)

        if battle_result == "tie":
            pass
        else:
            winner = user if battle_result == "user" else computer
            winner.win_cards(game_table.cards)
            game.announce_winner_of_round(battle_result)

        show_cards_of_players(user, computer)
        game.ask_user_to_play(game.round)


if __name__ == "__main__":
    main()
