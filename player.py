class Player:

    def __init__(self, name, first_card, second_card, first_card_score, second_card_score):
        self.name = name
        self.first_card = first_card
        self.second_card = second_card
        self.score = first_card_score + second_card_score
        print(f"\nAlright, {self.name}, your initial cards are the {self.first_card} and the {self.second_card}!")
        print(f"\nYour initial score is {self.score}!\n")

    def hit_me(self, new_card, new_card_score):
        self.score += new_card_score
        print(f'\nAlright, {self.name}, your next card is the {new_card}!')
        print(f'\nYour new score is {self.score}!\n')