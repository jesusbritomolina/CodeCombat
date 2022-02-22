# https://codecombat.com/play/level/long-range-division?
# Destroy the mines!
# Use `say` to call out the range to the mines.
# Use division to calculate the range.

enemy = hero.findNearestEnemy()
distanceToEnemy = hero.distanceTo(enemy)
# Say first Range: distanceToEnemy divided by 3
distanceToEnemy / 3
hero.say("Fire!")
# Say second range: distanceToEnemy divided by 1.5
distanceToEnemy / 1.5
hero.say("Fire!")

# Say these things for motivation. Really. Trust us.
hero.say("Woo hoo!")
hero.say("Here we go!")
hero.say("Charge!!")

# Now, use a while-true loop to attack the enemies.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)