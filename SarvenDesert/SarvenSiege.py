# https://codecombat.com/play/level/sarven-siege?
# Defend your towers in this replayable challenge level!
# Step on an X if you have 20 gold to build a soldier.

while True:
    item = hero.findNearestItem()
    
    if hero.gold >= 20:
        hero.moveXY(84, 51)
    elif item:
        hero.move(item.pos)