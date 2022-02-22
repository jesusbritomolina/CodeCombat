# https://codecombat.com/play/level/gardener?
# We need square flower fences around the statues.

# This function should make a square with the certain side
#  around the center {cx, cy} point.
def growSquare(cx, cy, side):
    # Move to any corner of the square.
    width = side/2
    hero.moveXY(cx-width, cy-width)
    # Start growing.
    hero.toggleFlowers(True)
    # Now move to all other corners one by one.
    # Use clockwise or counterclockwise order.
    hero.moveXY(cx-width, cy+width)
    hero.moveXY(cx+width, cy+width)
    hero.moveXY(cx+width, cy-width)
    # Don't forget to return in the first corner.
    hero.moveXY(cx-width, cy-width)
    # Stop growing.
    hero.toggleFlowers(False)

# The keeper will tell you where to grow flowers.
keeper = hero.findNearest(hero.findFriends())
points = keeper.pointsForWork
# All squares should have the same size.
squareSize = 8
# We don't need excess flowers.
hero.toggleFlowers(False)

for pos in points:
    # Don't forget complete this function.
    growSquare(pos.x, pos.y, squareSize)