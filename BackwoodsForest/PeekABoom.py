# https://codecombat.com/play/level/peek-a-boom?
# Build traps on the path when the hero sees a munchkin!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Build a "fire-trap" at the Red X (41, 24)
        hero.buildXY("fire-trap", 41, 24)
        pass
    # Add an else below to move back to the clearing
    else:
        # Move to the Wooden X (19, 19)
        hero.moveXY(19, 19)