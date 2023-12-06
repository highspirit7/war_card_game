# War(card game)

## 1. Rule
> There may be many variations to this game, but the rules for this game are set out below.

> The ranks of cards : A(Ace) is the highest and suits(heart, spade, club, diamond)are ignored.

War(card game) is a fun card game where players try to win all of the cards in the deck.

This game uses one standard deck of playing cards.(the version of this war game does not use joker cards, so the total number of cards for this game is 52.)

First, all the cards are evenly dealt between the players. So every player has the same number of cards.

Each player keeps their cards face down in a pile in front of them. Then all players flip the top cards on their pile face up on the table at the same time.

The player who has the highest card wins all of the cards on the table and places them face down at the bottom of their pile.(Before placing cards at the bottom of a pile, they should be shuffled.)

But, two or more players flip a card in the same rank, they go to ‘war’. 

At the ‘war’, each player in the war places the top 3 card face down on the table and flip 4th card and place it face up on the table as well.

Whoever has the highest face up card wins all of the cards on the table. 
If there are face up cards in the same rank at the ‘war’, another ‘war’ would go on in the same manner until one player wins the war.

If a player does not have enough cards for the war, the player loses the war and loses his(or her) cards on the table.

Once a player has no cards to play, then the player will be eliminated from this card game.

This game continues until one player wins all of the cards in the deck.

## 2. Requirements(or Implementation)
### 2.1 Game Initialization
- User play against a computer. So 2 players play war card game in this program.
- The program shall initialize a standard deck of 52 playing cards.(without joker cards)
- The deck shall be shuffled before the start of each game.
- The cards shall be distributed equally between all players.
### 2.2 Game Mechanics
The game shall consist of a series of rounds.
Each round shall involve the player and the computer playing a card.
The card with the higher rank wins the round.
In the event of a tie, a "war" shall occur, and additional cards will be drawn until a winner is determined.
### 2.3 User Interface
The program shall provide a console-based user interface for interaction.

- User will be asked to continue playing after each round. So user can stop playing this card game by replying 'No' for this question.

The user shall receive prompts and instructions for playing the game.
Game progress(e.g. the number of cards left for user and computer, which cards are on the table in each round and so on) shall be displayed clearly.
### 2.4 End of Game
The game shall continue until user or computer wins all the cards.
The program shall declare the winner when the game ends.

## 3. Class Structure
https://pourmavie.notion.site/Necessary-Classes-OOP-7399cfe8ed75483ca71e6b0820b60dcd?pvs=4
