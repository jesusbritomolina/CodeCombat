# https://codecombat.com/play/level/tactical-strike?
# Defeat the ogres.
hero.moveDown()
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveDown()