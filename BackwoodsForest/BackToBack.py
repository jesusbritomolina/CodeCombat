# https://codecombat.com/play/level/back-to-back?
# Permanece en el medio y defiende!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Ya sea cualquiera de atacar al enemigo ...
        hero.attack(enemy)
        pass
    else:
        # o volver a tu posición defensiva.
        hero.moveXY(40, 33)
        pass