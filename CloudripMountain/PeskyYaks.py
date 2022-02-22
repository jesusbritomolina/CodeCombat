# https://codecombat.com/play/level/pesky-yaks?
# That's a lot of Yaks!
# If you are to survive, you'll need to filter out Yaks...
def removeByType(enemies, excludedType):
    tempList = []
    # Go through each enemy and check to see if its type is excludedType.
    for enemy in enemies:
        # If it isn't, 'append' it to the list.
        if enemy.type != excludedType:
            tempList.append(enemy)
        pass
    return tempList

while True:
    # Find the enemies!
    enemies = hero.findEnemies()
    # Remove those pesky Yaks.
    enemies = removeByType(enemies, "sand-yak")
    enemy = hero.findNearest(enemies)
    if enemy:
        # Now... 'remove' those enemies.
        hero.attack(enemy)