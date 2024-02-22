from cards.card import Card, CardType


class Slimed(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.STATUS
        self.cost = 1
        self.dmg = 0
        self.vulnerable = 0

    def play(self):
        self.exhaust()
