# https://codecombat.com/play/level/long-road?
# Move to the right.

# Complete this function:
def onSpawn(event):
    pass
    # Inside a while-true while True:
    while True:
        # Use hero.findNearestItem()
        item = hero.findNearestItem()
        # If there's an item:
        if item:
            # Use pet.fetch(item) to fetch the item.
            pet.fetch(item)

# Use pet.on() to assign onSpawn to the "spawn" event
pet.on("spawn", onSpawn)
hero.moveXY(78, 35)