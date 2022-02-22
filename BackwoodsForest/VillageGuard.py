# https://codecombat.com/play/level/village-guard?
# Patrol the village entrances.
# If you find an enemy, attack it.
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # Now move to the right entrance.
    hero.moveXY(60, 32)
    # Use findNearestEnemy again to find the right enemy.
    rightEnemy = hero.findNearestEnemy()
    # Use "if" to attack twice if there is a right enemy.
    if rightEnemy:
        hero.attack(rightEnemy)
        hero.attack(rightEnemy)