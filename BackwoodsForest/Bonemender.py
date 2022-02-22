# https://codecombat.com/play/level/bonemender?
# Heal allied soldiers to survive the siege.
while True:
    if hero.canCast("regen"):
        bernardDistance = hero.distanceTo("Bernard")
        if bernardDistance < 10:
            # "Bernard" needs regeneration!
            hero.cast("regen", "Bernard")
        
        # Use "if" and "distanceTo" to regenerate "Chandra"
        # if she is closer than 10 meters away.
        distance = hero.distanceTo("Chandra")
        
    else:
        # If you aren't casting "regen", use "if" and "distanceTo"
        # to attack enemies that are closer than hero.attackRange.
        hero.attackRange
        pass