# https://codecombat.com/play/level/swift-dagger?
# Use your bow at long range and dagger at short range.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < hero.throwRange:
            # Throw your dagger at the enemy if "throw" is ready.
            hero.throw(enemy)
        else:
            # Attack the enemy with your bow.
            hero.attack(enemy)