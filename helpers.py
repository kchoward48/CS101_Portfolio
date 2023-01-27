import pyfiglet
import random
from game import Game

# Exception handler function 'get_ace_value', called when the card is an ambiguous ace value.
def get_ace_value(name, card_num, second_card = '', second_card_score = 0):
    ace_value = 0
    while ace_value != 1 and ace_value != 11:
        # Perform exception handling, in case of invalid input:
        try:
            if second_card != '':
                ace_value = int(input(f"\nHey, {name}, your {card_num} card is an ace! Would you like to use it " + \
                f"as a '1' or an '11'? By the way, your first card was a {second_card}, giving you a current score of " + \
                    f"{second_card_score}: "))
            else:
                ace_value = int(input(f"\nHey, {name}, your {card_num} card is an ace! Would you like to use it " + \
                "as a '1' or an '11'? "))
            if ace_value != 1 and ace_value != 11:
                print("\nOops! You didn't enter '1' or '11'; please try again!")
                continue
            return ace_value
        except ValueError:
            print("\nOops! You didn't enter a number; please try again!")

# Helper function 'play_round' simulates one complete round; if a 'Player' wins during the round, the function immediately
# 'return's to the main function, and 'return's once more out of the 'Round 2-N' while loop, ending the game and program.
def play_round(player_list):
    temp_stopped_player_list = []
    remove_player_list = []
    for player in player_list:
        hit_response = str.lower((input(f"\nAlright, {player.name}, your score is currently {player.score}; type any character " + \
            "to hit, or just type 'Enter' to stop! ")))
        if hit_response != '':
            new_card = random.choice(list(Game.dict_of_cards.keys()))
            new_card_value = Game.dict_of_cards.pop(new_card)
            if new_card[0:3] == 'ace':
                new_card_value = get_ace_value(player.name, 'next')
            player.hit_me(new_card, new_card_value)
            if player.score > 21:
                print(f"I'm so sorry, {player.name}, you exceeded a score of '21'; good try, maybe next game!\n")
                remove_player_list.append(player)
            elif player.score == 21:
                congratulate_winner(player)
                return (False, False, False)
        else:
            print(f"\nAlright, {player.name}, you finish your run at a score of '{player.score}'!\n")
            temp_stopped_player_list.append(player)

    return (player_list, temp_stopped_player_list, remove_player_list)

# Helper function 'print_current_score', which gives each current 'Player's score after a given round:
def print_current_score(player_list, stopped_player_list, round):
    print(f'\nAlright, after {round} rounds, the score is currently: \n')
    for player in player_list:
        print(f'{player.name}: {player.score}\n')
    for player in stopped_player_list:
        print(f'{player.name}: {player.score}\n')

# Additional helper functions:

def congratulate_winner(player):
    print('\n')
    print(pyfiglet.figlet_format("Blackjack", font = "bubble", width = 75))
    print(f"\n\nCongratulations, {player.name}, you have scored exactly '21' and are the first to do so!")
    print(f"\nWhich means you are the winner of this game of Blackjack! Congratulations!")
    print('\n')

def announce_winner(stopped_player_list):
    # Assuming no one reached 21 after the 'player_list' has been emptied, announce the winner from the 'stopped_player_list':
    top_score = 0
    player_rank_list = []
    for player in stopped_player_list:
        print(f'\n\nAlright, {player.name}, you finish the game with a score of {player.score}!')
        if player.score >= top_score:
            top_score = player.score
            player_rank_list.append(player)
    
    if len(player_rank_list) > 1:
        if player_rank_list[-1].score == player_rank_list[-2].score:
            print('\n')
            print(pyfiglet.figlet_format(f'This game has ended in a tie!', font = "alligator", width = 75))
            return

    print(pyfiglet.figlet_format(f'\nCongratulations, {player_rank_list[-1].name}, you win!', font = "drpepper", width = 75))
    print('\n\n')