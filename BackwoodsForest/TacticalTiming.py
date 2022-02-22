# https://codecombat.com/play/level/tactical-timing?
# Help out on the front line.
# Move back to a flag if any try to sneak by.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    elif hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)