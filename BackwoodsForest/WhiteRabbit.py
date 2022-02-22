# https://codecombat.com/play/level/white-rabbit?
# Follow the lightstone to navigate the traps.

while True:
    item = hero.findNearestItem()
    if item:
        # Store the item's position in a new variable using item.pos:
        hero.moveXY(item.pos.x, item.pos.y)
        # Store the X and Y coordinates using pos.x and pos.y:
        itemx = item.pos.x
        itemy = item.pos.y
        # Move to the coordinates using moveXY() and the X and Y variables:
        hero.moveXY(itemx, itemy)
        pass