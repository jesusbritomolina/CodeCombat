# https://codecombat.com/play/level/misty-island-mine?
# Collect gold efficiently by commanding peasants wisely!
# Peasants should collect coins and build decoys.

# The function should return the best item per target
# Use an array of ids to ensure no two peasants target the same item.
def findBestItem(friend, excludedItems):
    items = friend.findItems()
    bestItem = None
    bestItemValue = 0
    for item in items:
        # Use in to check if an element is in the excludedItems array.
        # In that case, skip over that item as another peasant is targeting it.
        if item in excludedItems:
            continue
        # Finish the function!
        # Remember bestItemValue should be the highest item.value / distanceTo
        if item not in excludedItems:
            if bestItemValue < item.value / friend.distanceTo(item):
                bestItemValue = item.value / friend.distanceTo(item)
                bestItem = item
    return bestItem

# This function checks if you have enough gold for a decoy.
def enoughGoldForDecoy():
    return hero.gold >= 25

while True:
    peasants = hero.findByType("peasant")
    # Create a new array every loop.
    claimedItems = []
    for peasant in peasants:
        enemy = peasant.findNearestEnemy()
        if enemy:
            # If the peasant is the target of the enemy
            # AND the hero has enough gold for a decoy
            if hero.gold > 25:
                # Command a peasant to build a "decoy":
                hero.command(peasant, 'buildXY', 'decoy', peasant.pos.x, peasant.pos.y)
                # Add a continue so the peasant doesn't collect coins when building.
                continue
            pass
        item = findBestItem(peasant, claimedItems)
        if item:
            # After an item is claimed, stick it in the claimedItems array.
            claimedItems.append(item)
            # Command the peasant to collect the coin:
            hero.command(peasant, 'move', item.pos)