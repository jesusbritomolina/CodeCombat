# https://codecombat.com/play/level/yakstraction?
# Protect brandy from incoming thirsty yaks!
# Gather gold to build decoys to distract the yaks.
# Use flags to decide when and where to build decoys.

while True:
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    if hero.gold >= 25:
        hero.buildXY("decoy", hero.pos.x, hero.pos.y)