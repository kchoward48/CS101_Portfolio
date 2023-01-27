import pyfiglet
import random
import helpers
from game import Game
from player import Player
"""
Objective: Create an interactive game of Blackjack.

Some House Rules: 

1) Very first player to '21' wins, no exceptions!
2) If a player receives an ace on their first card in the initial round, they must determine whether to make it worth '1' or '11'
   before being dealt their second card.

"""

def main():
    player_list = []
    stopped_player_list = []
    result = pyfiglet.figlet_format("Blackjack", font = "3-d")
    print(result)
    print('---------------------')
    print('Welcome to Blackjack!')
    print('---------------------')
    game_1 = Game()
    print(game_1)
    while True:
        try:
            num_players = int(input('How many players do we have for this game? '))
            break
        except ValueError:
            print("\nOops! You didn't enter a number; please try again!\n")
            continue
    print(f'\nAlright, there are {num_players} players for this game! \n')

    # Round 1 (Initial):
    for i in range(0, num_players):
        ace_value_1 = 0
        ace_value_2 = 0
        name = str(input(f"\nAlright, what is Player #{i + 1}'s name? "))
        card_1 = random.choice(list(Game.dict_of_cards.keys()))
        card_1_value = Game.dict_of_cards.pop(card_1)
        card_2 = random.choice(list(Game.dict_of_cards.keys()))
        card_2_value = Game.dict_of_cards.pop(card_2)
        if card_1[0:3] == 'ace':
            card_1_value = helpers.get_ace_value(name, 'first')
        if card_2[0:3] == 'ace':
            card_2_value = helpers.get_ace_value(name, 'second', card_1, card_1_value)
        player_list.append(Player(name, card_1, card_2, card_1_value, card_2_value))
        # If the 'Player' wins in the initial round, end the game, and thus the program by 'return'ing in 'main':
        if player_list[i].score > 21:
            print(f"I'm so sorry, {player.name}, you exceeded a score of '21'; good try, maybe next game!\n")
            remove_player_list.append(player)
        elif player_list[i].score == 21:
            helpers.congratulate_winner(player_list[i])
            return

    # Rounds 2-N:
    round = 2
    while len(player_list) > 0:
        remove_player_list = []
        player_list, temp_stopped_player_list, remove_player_list = helpers.play_round(player_list)
        if (player_list == False and temp_stopped_player_list == False and remove_player_list == False): return
        if len(remove_player_list) != 0:
            for player in remove_player_list:
                player_list.remove(player)
        if len(temp_stopped_player_list) != 0:    
            for player in temp_stopped_player_list:
                stopped_player_list.append(player)
                player_list.remove(player)
        helpers.print_current_score(player_list, stopped_player_list, round)
        round += 1

    # Time to announce the winner!
    helpers.announce_winner(stopped_player_list)

if __name__ == "__main__":
    main()