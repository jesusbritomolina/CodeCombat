# https://codecombat.com/play/level/explosive-works?
# Place explosives to clear a passage to the dungeon.

# The mines should form a rectangle with this perimeter.
perimeter = 160
area = 0
# The bottom left corner of the rectangle.
bottomLeft = {"x": hero.pos.x, "y": hero.pos.y}

# One mine is placed already.
topLeft = hero.findHazards()[0].pos
# So we can find the height of the rectangle.
height = hero.distanceTo(topLeft)
# Find the width. Use the perimeter and height to calculate it.
width = (perimeter - height*2)/2

# First, we need to place a mine in the bottom left corner.
hero.buildXY("fire-trap", bottomLeft.x, bottomLeft.y)
# Put a mine in the bottom right corner.
hero.buildXY("fire-trap", bottomLeft.x+width, bottomLeft.y)
# Put a mine in the top right corner.
hero.buildXY("fire-trap", bottomLeft.x+width, topLeft.y)

# Now go to the demolitionist.
hero.moveXY(74, 32)
# Calculate the area of the rectangle to know the charge.
area = width*height
# Say the area of the rectangle to start the explosion.
hero.say(area)