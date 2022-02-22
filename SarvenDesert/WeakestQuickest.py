# https://codecombat.com/play/level/weakest-quickest?
# Defeat shamans to survive.

# This function finds the weakest enemy.
def findWeakestEnemy():
    enemies = hero.findEnemies()
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    # Loop through enemies:
    while enemyIndex < len(enemies):
        # If an enemy's health is less than leastHealth:
        enemy = enemies[enemyIndex]
        enemyIndex += 1
        if enemy.health < leastHealth:
            # Make it the weakest 
            weakest = enemy
            # and set leastHealth to its health.
            leastHealth = enemy.health
    return weakest

while True:
    # Find the weakest enemy with the function:
    weakestShaman = findWeakestEnemy()
    # If the weakest enemy exists:
    if weakestShaman:
        # Attack it!
        hero.attack(weakestShaman)