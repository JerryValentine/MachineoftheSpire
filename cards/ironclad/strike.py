from cards.card import Card, CardType
from units.unit import Unit


class Strike(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.ATTACK
        self.cost = 1
        self.dmg = 6

    def upgrade(self):
        self.dmg = 9

    def play(self, **units: Unit):
        dmg = self.calculate_dmg(units['player'], units['target'])
        units['target'].take_dmg(dmg)
