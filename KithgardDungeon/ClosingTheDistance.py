# https://codecombat.com/play/level/closing-the-distance?
hero.moveRight()

# You should recognize this from the last level.
enemy1 = hero.findNearestEnemy()
# Now attack enemy1.
hero.attack(enemy1)

hero.moveRight()
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.moveRight(2)