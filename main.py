from units.enemies.standard import jaw_worm

enemy = jaw_worm.JawWorm()
enemy2 = jaw_worm.JawWorm()
# print(enemy.hp)
# print(enemy2.hp)
# enemy.act(2)
# print(enemy2.hp)

round_1 = enemy.get_action(round=2)
round_2 = enemy.get_action(round=3)
round_3 = enemy.get_action(round=4)
round_4 = enemy.get_action(round=5)
round_5 = enemy.get_action(round=6)
round_6 = enemy.get_action(round=7)
round_7 = enemy.get_action(round=8)

print(round_1())
print(round_2())
print(round_3())
print(round_4())
print(round_5())
print(round_6())
print(round_7())

print('end turn')

print(round_1(is_acting=True))
print(round_2(is_acting=True))
print(round_3(is_acting=True))
print(round_4(is_acting=True))
print(round_5(is_acting=True))
print(round_6(is_acting=True))
print(round_7(is_acting=True))
print(enemy.sheild)
print(enemy.strength)
