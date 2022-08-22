class Player:
    def __init__(self, sub_deck, name):
        self.deck = sub_deck
        self.name = name

    def extract_card(self):
        return self.deck.pop(0)

    def win_cards(self, cards_win):
        self.deck += cards_win

    def cards_left(self):
        return len(self.deck)
