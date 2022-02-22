# https://codecombat.com/play/level/patrol-buster?
# Remember that enemies may not yet exist.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Si hay un enemigo, atacarlo!
        hero.attack(enemy)
        pass