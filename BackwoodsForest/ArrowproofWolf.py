# https://codecombat.com/play/level/arrowproof-wolf?
# Collect mushrooms.

# First, come to the wolf pet and wake up it (say).
hero.moveXY(12, 34)
hero.say("wake up")
# Next collect mushrooms just usual items.
while True:
    item = hero.findNearestItem()
    if item:
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.moveXY(x, y)