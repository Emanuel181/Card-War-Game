import constants
import random
import card_class


class Deck:
    def __init__(self):
        self.card_list = [card_class.Card(suit, rank) for rank in constants.ranks for suit in constants.suits]
        random.shuffle(self.card_list)
