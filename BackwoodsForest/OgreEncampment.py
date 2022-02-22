# https://codecombat.com/play/level/ogre-encampment?
# If there is an enemy, attack it.
# Otherwise, attack the chest!

while True:
    enemy = hero.findNearestEnemy()
    # Use if/else.
    if enemy:
        hero.attack(enemy)
    else:
        hero.attack("Chest")