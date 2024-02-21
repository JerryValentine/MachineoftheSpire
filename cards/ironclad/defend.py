from cards.card import Card, CardType
from units.unit import Unit


class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.SKILL
        self.cost = 1
        self.block = 5

    def upgrade(self):
        self.block = 8

    def play(self, **units: Unit):
        units['player'].shield += (self.block + units['player'].dexterity)
