# https://codecombat.com/play/level/brown-noise?
# Collect the treasure and escape.

# Prepare the hero and the pet.
pet.moveXY(32, 28)
hero.moveXY(10, 19)
# Distract the skeleton.
pet.distractionNoise()
# Sneak while the skeleton is distracted.
hero.moveXY(10, 20)

hero.moveXY(10, 46)
pet.moveXY(hero.pos.x, hero.pos.y)
hero.moveXY(47, 48)
hero.moveXY(46, 35)
pet.moveXY(64, 28)
pet.distractionNoise()


# Repeat this maneuver to get the treasure:
hero.moveXY(46, 10)
hero.moveXY(70, 9)


# Escape from the dungeon (the red mark):
hero.moveXY(47, 8)

hero.moveXY(46, 18)
pet.distractionNoise()
hero.moveXY(46, 31)
hero.moveXY(47, 48)
hero.moveXY(40, 56)