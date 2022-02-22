# https://codecombat.com/play/level/distraction-maneuver?
# Protect the peasants!

# This is like findNearestEnemy but vice versus.
def findFurthestEnemy():
    enemies = hero.findEnemies()
    furthestEnemy = None
    maxDistance = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        currentEnemy = enemies[enemyIndex]
        # Find the distance to currentEnemy:
        distance = hero.distanceTo(currentEnemy)
        # If that distance greater than maxDistance:
        if distance > maxDistance:
            # Reassign furthestEnemy to currentEnemy:
            furthestEnemy = currentEnemy
            # Reassign maxDistance to the distance:
            maxDistance = distance
        enemyIndex += 1
    return furthestEnemy
    

while True:
    # To protect peasants, hunt for furthest ogres.
    furthestOgre = findFurthestEnemy()
    if furthestOgre:
        while furthestOgre.health > 0:
            hero.attack(furthestOgre)