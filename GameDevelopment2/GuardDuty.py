# https://codecombat.com/play/level/guard-duty?
# Add a soldier to the level to prevent ogres from crossing the path.
# Command the soldier using an event handler function.

def soldierLogic():
    # Fill in the code for the soldier's actions here.
    # Remember to use 'soldier' instead of 'hero'!
    while True:
        enemy = soldier.findNearestEnemy()
        # Attack the enemy, if the enemy exists.
        if enemy:
            # Units have the attack() method.
            # Use soldier.attack(enemy) method:
            soldier.attack(enemy)
            pass
        # Else, move back to the starting position.
        else:
            # Units have the moveXY() method.
            soldier.moveXY(42,48)
            pass

# This assigns your spawned unit to the soldier variable.
soldier = game.spawnXY("soldier", 42, 48)
# This says to run the soldierLogic function when the soldier is spawned.
soldier.on("spawn", soldierLogic)