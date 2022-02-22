# https://codecombat.com/play/level/storming-the-farmhouse?
# Soldiers will slowly arrive, but the ogres will overwhelm them.
# A basic attack loop isn't going to be enough to keep you alive.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag and hero.isReady("cleave"):
        hero.pickUpFlag(flag)
        hero.cleave(enemy)
    elif enemy:
        hero.attack(enemy)