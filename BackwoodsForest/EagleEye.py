# https://codecombat.com/play/level/eagle-eye?
# Remember that enemies may not yet exist.
while True:
    enemy = hero.findNearestEnemy()
    # Si hay un enemigo, atacarlo!
    if enemy:
        hero.attack(enemy)