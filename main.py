from units.player import Player
from units.enemies.standard.jaw_worm import JawWorm
from cards.ironclad.strike import Strike

# Object Instantiation

player = Player(100)
strike = Strike()
enemy = JawWorm()
enemy2 = JawWorm()


# Enemy Testing

# round_1 = enemy.get_action(round=2)
# round_2 = enemy.get_action(round=3)
# round_3 = enemy.get_action(round=4)
# round_4 = enemy.get_action(round=5)

# print(round_1())
# print(round_2())
# print(round_3())
# print(round_4())
# print(round_5())
# print(round_6())
# print(round_7())

# print('end turn')

# print(round_1(is_acting=True))
# print(round_2(is_acting=True))
# print(round_3(is_acting=True))
# print(round_4(is_acting=True))
# print(enemy.shield)
# print(enemy.strength)


# Card testing

print(enemy)
strike.play(player, enemy)
strike.play(player, enemy)
strike.play(player, enemy)
print(enemy)
