from table import Table
from card import (
    compare_two_cards,
    ascii_of_two_cards,
    ascii_of_cards_for_war,
)
from war_game import WarGame, get_winner_of_game, check_cards_before_war
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

        game_table = Table([user_top_card], [computer_top_card])
        game_table.top_table_of_battle(game.round)
        ascii_of_two_cards(user_top_card, computer_top_card)
        game_table.bottom_of_table("battle")

        battle_result = compare_two_cards(user_top_card, computer_top_card)
        war_result = None

        if battle_result == "tie":
            # before going to war, need to check if all players have enough cards for war
            while not game_table.is_war_over:
                result = check_cards_before_war(user.card_pile, computer.card_pile)

                if result != "continue":
                    game.announce_winner_of_game(result)
                    game.exit_war_game()

                war_result = go_to_war(game, game_table, user, computer)

                if war_result != "tie":
                    game_table.is_war_over = True

        result_of_round = battle_result if war_result == None else war_result
        winner = user if result_of_round == "user" else computer
        winner.win_cards(game_table.cards)
        game.announce_winner_of_round(result_of_round)

        show_cards_of_players(user, computer)

        # check each player's deck in order to find if we have a winner in this whole game after each round
        winner = get_winner_of_game(user.card_pile, computer.card_pile)
        if winner != None:
            game.announce_winner_of_game(winner)
            game.exit_war_game()

        game.ask_user_to_play(game.round)


def go_to_war(game: WarGame, game_table: Table, user: Player, computer: Player):
    game.announce_war()
    game_table.war_count += 1
    game_table.top_table_of_war(game.round)

    this_war_user_cards = user.flip_cards_for_war()
    this_war_computer_cards = computer.flip_cards_for_war()
    game_table.cards.extend(this_war_user_cards + this_war_computer_cards)
    game_table.user_cards.extend(this_war_user_cards)
    game_table.computer_cards.extend(this_war_computer_cards)

    ascii_of_cards_for_war(this_war_user_cards, this_war_computer_cards)
    game_table.bottom_of_table("war")

    return compare_two_cards(game_table.user_cards[-1], game_table.computer_cards[-1])


if __name__ == "__main__":
    main()
