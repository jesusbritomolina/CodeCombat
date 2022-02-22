# https://codecombat.com/play/level/gas-attack?
# Calculate the total health of all the ogres.

def sumHealth(enemies):
    # Create a variable and set it to 0 to start the sum.
    totalHealth = 0
    # Initialize the loop index to 0
    enemyIndex = 0
    # While enemyIndex is less than the length of enemies array
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # Add the current enemy's health to totalHealth
        totalHealth += enemy.health
        # Increment enemyIndex by 1.
        enemyIndex += 1
    return totalHealth

# Use the cannon to defeat the ogres.
cannon = hero.findNearest(hero.findFriends())
# The cannon can see through the walls.
enemies = cannon.findEnemies()
# Calculate the sum of the ogres' health.
ogreSummaryHealth = sumHealth(enemies)
hero.say("Usar " + ogreSummaryHealth + " grams.")