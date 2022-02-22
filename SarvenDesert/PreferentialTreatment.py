# https://codecombat.com/play/level/preferential-treatment?
# First, loop through all enemies...

enemies = hero.findEnemies()
enemyIndex = 0
# ... but only attack "thrower" type enemies.
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy and enemy.type == "thrower":
        hero.attack(enemy)
    enemyIndex += 1
# Then loop through all the enemies again...
enemies = hero.findEnemies()
enemyIndex = 0
# ... and defeat everyone who's still standing.
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy:
        hero.attack(enemy)
    enemyIndex += 1