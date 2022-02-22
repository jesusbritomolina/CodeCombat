# https://codecombat.com/play/level/forest-miners?
# Check if the mines are safe for the workers.

def checkEnemyOrSafe(target):
    # If `target` (the parameter) exists:
    if target:
        # Then attack target.
        hero.attack(target)
    # Otherwise:
    else:
        # Use say() to call the peasants.
        hero.say("Hi")
    pass

while True:
    # Move to, and check the top right X mark.
    hero.moveXY(64, 54)
    enemy1 = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy1)
    
    # Move to the bottom left X mark.
    hero.moveXY(16, 14)
    # Save the result of findNearestEnemy() in a variable.
    enemy2 = hero.findNearestEnemy();
    # Call checkEnemyOrSafe, and pass the
    # result of findNearestEnemy as the argument.
    checkEnemyOrSafe(enemy2)