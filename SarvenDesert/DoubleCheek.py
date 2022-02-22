# https://codecombat.com/play/level/double-cheek?
# First, defeat 6 ogres.
# Then collect coins until you have 30 gold.

# This variable is used for counting ogres.
defeatedOgres = 0

# This loop is executed while defeatedOgres is less than 6.
while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        defeatedOgres += 1
    else:
        hero.say("Ogres!")

# Move to the right side of the map.
hero.moveXY(49, 36)

# This loop is executed while you have less than 30 gold.
while hero.gold < 30:
    # Find and collect coins.
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    # Remove this say() message.


# Move to the exit.
hero.moveXY(76, 32)