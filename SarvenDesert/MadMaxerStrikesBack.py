# https://codecombat.com/play/level/mad-maxer-strikes-back?
# The smaller ogres here do more damage!
# Attack the ogres with the least health first.
while True:
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Loop through all enemies.
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # If an enemy's health is less than leastHealth,
        if enemy.health < leastHealth:
            # make it the weakest and set leastHealth to its health.
            weakest = enemy
        #  Don't forget to increase enemyIndex by 1.
        enemyIndex += 1
    if weakest:
        # Attack the weakest ogre.
        hero.attack(weakest)
        pass