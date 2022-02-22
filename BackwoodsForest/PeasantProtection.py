# https://codecombat.com/play/level/peasant-protection?
while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # Ataca si se acercan demasiado al campesino.
        hero.attack(enemy)
        pass
    # De lo contrario, ¡quédate cerca del campesino¡ Usa else
    else:
        hero.moveXY(40, 37)