# https://codecombat.com/play/level/teleport-lasso?
# Our wizards teleport ogres from their camp here.
# They appear for a short period and they are stunned.
# Attack only weak and near ogres.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # If enemy.type is "munchkin"
    # AND the distance to it is less than 20m
    if enemy.type == "munchkin" and distance < 20:
        # Then attack it.
        hero.attack(enemy)