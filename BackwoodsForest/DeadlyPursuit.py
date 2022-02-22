# https://codecombat.com/play/level/deadly-pursuit?
# Grab all the coins and use flags to build traps behind
# you to deal with those ogres.

while True:
    flag = hero.findFlag()
    item = hero.findNearestItem()
    if flag:
        flagPos = flag.pos
        flagx = flagPos.x
        flagy = flagPos.y
        hero.buildXY("fire-trap", flagx, flagy)
        hero.pickUpFlag(flag)
        
    elif item:
        itemPos = item.pos
        itemx = itemPos.x
        itemy = itemPos.y
        hero.moveXY(itemx, itemy)