# https://codecombat.com/play/level/backwoods-ambush?
hero.moveXY(24, 42)
enemy = hero.findNearestEnemy()
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(27, 60)
enemy = hero.findNearestEnemy()
if enemy:
    # Attack the enemy if it exists!
    hero.attack(enemy)
    pass # `pass` is a placeholder.

hero.moveXY(42, 50)
enemy = hero.findNearestEnemy()
# Use an if-statement to check if an enemy exists.
if enemy:
    # Attack the enemy if it exists!
    hero.attack(enemy)

hero.moveXY(39, 24)
# Find the nearest enemy:
enemy = hero.findNearestEnemy()
# Check if the enemy exists:
if enemy:
    # Attack the enemy if it exists!
    hero.attack(enemy)