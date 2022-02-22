# https://codecombat.com/play/level/the-agrippa-defense?
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        pass  # Replace this with your own code.
        # Find the distance to the enemy with distanceTo.
        distance = hero.distanceTo(enemy)
        # If the distance is less than 5 meters...
        if distance < 5:
            # ... if "cleave" is ready, cleave!
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            # ... else, just attack.
            else:
                hero.attack(enemy)