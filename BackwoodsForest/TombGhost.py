# https://codecombat.com/play/level/tomb-ghost?
# The only exit is blocked by ogres.
# Hide from the skeletons and defeat the ogres one by one.

# This function should attack an enemy and hide.
def hitOrHide(target):
    # If 'target' exists:
    if target:
        # Attack 'target'.
        hero.attack(target)
        # Then move to the red mark.
        hero.moveXY(32, 17)
    pass

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)