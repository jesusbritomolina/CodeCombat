# https://codecombat.com/play/level/shrapnel?
# Use charges to soften up packs of ogres.
# Then pick them off with your bow.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("throw"):
            distance = hero.distanceTo(enemy)
            # Only throw if the ogres are more than 15m away.
            # Use "if" to compare distance to 15.
            if distance < 15:
            # Use "else" to attack if you're not throwing.
                hero.attack(enemy)
            else:
                hero.attack(enemy)