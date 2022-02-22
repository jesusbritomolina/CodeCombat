# https://codecombat.com/play/level/count-links?
# Each cannon fires 1 to 5 shells, all at once, one time.
# The first (index 0) has 1, the second has 2, and so on.

# Find the element by index in a linked list.
def elementByIndex(linkedList, index):
    current = linkedList
    # Iterate from 0 to "index" (exclusive):
    for i in range(index):
        # Each element links to the next element.
        # Reassign "current" with current.next
        current = current.next
        # If the current element is empty, break here:
        if not(current):
            break
    # Return the current element.
    return current

# The reference to the linked list of cannons.
cannonList = hero.findNearest(hero.findFriends())

while True:
    enemies = hero.findEnemies()
    if len(enemies) > 0:
        # Find the cannon that has enough shells:
        hero.say(elementByIndex(cannonList, len(enemies) - 1))