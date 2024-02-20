from units.unit import Unit


class Player(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.confused = False
        self.dexterity = 0
        self.dexterity_down = 0
        self.stength_down = 0
        self.frail = 0
        self.no_draw = False
        self.constricted = 0
        self.draw_reduction = 0
        self.entangled = False
        self.hex = False
        self.no_block = 0
