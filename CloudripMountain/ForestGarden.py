# https://codecombat.com/play/level/forest-garden?
# Grow the perfect rectangular flower fence.

# Use the given dimensions for the flower rectangle.
gardener = hero.findNearest(hero.findFriends())
gardenWidth = gardener.gardenWidth
gardenHeight = gardener.gardenHeight
# Start the flower fence at the initial position.
hero.toggleFlowers(True)
x = hero.pos.x
y = hero.pos.y
# Use variables gardenWidth and gardenHeight to get corners' coordinates.
# Move to each corner, one by one, and return to the start:
hero.moveXY(x+gardenWidth, y)
hero.moveXY(x+gardenWidth, y-gardenHeight)
hero.moveXY(x, y-gardenHeight)
hero.moveXY(x, y)