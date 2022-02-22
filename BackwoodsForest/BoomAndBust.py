# https://codecombat.com/play/level/boom-and-bust?
# Use your buildXY hammer to build two "fire-trap"s near the gate.
# They will detonate when you move back to a safe distance!
# Then, make a run for the forest!

hero.buildXY("fire-trap", 35, 35)
hero.buildXY("fire-trap", 35, 29)

hero.moveXY(11, 30)
hero.moveXY(60, 30)