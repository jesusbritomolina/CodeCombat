# https://codecombat.com/play/level/operation-killdeer?
# Lure the ogres into a trap. These ogres are careful.
# They will only follow if the hero is injured.

# This function checks the hero's health 
# and returns a Boolean value.
def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False

while True:
    enemy = hero.findNearestEnemy()
    # Move to the X only if shouldRun() returns True
    if shouldRun() == True:
        hero.moveXY(75, 37)
    # Else, attack!
    else:
        hero.attack(enemy)