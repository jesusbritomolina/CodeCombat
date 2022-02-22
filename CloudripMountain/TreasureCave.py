# https://codecombat.com/play/level/treasure-cave?
# That ogre was defeated instantly! Better just avoid that yeti.

# We've hacked your fire-traps to go off after 5 seconds.
# The clearing to the north would be a good place for an explosive distraction.
# The yeti won't stay distracted forever, so hurry and grab the coins!
# After that run to the camp!
hero.buildXY("fire-trap", 64, 44)
hero.moveXY(44, 8)

hero.moveXY(20, 30)
while True:
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    else:
        hero.moveXY(68, 12)