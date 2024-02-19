from ..unit import Unit


class Enemy(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.poison = 0
        self.shackled = 0
        self.slow = 0
