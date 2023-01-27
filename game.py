class Game:

    def create_dict_of_cards():
        dict_of_cards = {}
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        mv_cards = ['ace']
        face_cards = ['king', 'queen', 'jack']
        num_cards = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        for suit in suits:
            for card in mv_cards:
                dict_of_cards[f'{card} of {suit}'] = 0
            for card in face_cards:
                dict_of_cards[f'{card} of {suit}'] = 10
            for card in num_cards:
                dict_of_cards[f'{card} of {suit}'] = card
        return dict_of_cards
    
    # Create the 'dict_of_cards' and store it as a class variable
    dict_of_cards = create_dict_of_cards()

    def __init__(self):
        pass

    def __repr__(self):
        description = "Welcome to Blackjack! This game is a good test of each player's greediness level. Each player will \n" + \
            "be dealt two cards, and their initial score will be given to them. The objective of Blackjack is to get as close \n" + \
                "to the score of '21' as possible, using as many cards as necessary. Once the game begins, going around the \n" + \
                    "table, the current player will enter any character if they would like another card (called a hit); if the \n" + \
                        "player does not hit, they will be given their score and will no longer receive additional cards. \n" + \
                            "Be warned, though, no player can exceed the '21' point total, or else, they automatically lose! \n" + \
                                "The first player to reach '21' points, or in the case where no player reaches 21 points, \n" + \
                                    "whichever player is closest to the score of '21', is the winner! \n\n" + \
                                            "LET US BEGIN!!! \n"
        return description