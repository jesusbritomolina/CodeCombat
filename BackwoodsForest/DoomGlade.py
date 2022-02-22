# https://codecombat.com/play/level/doom-glade?
# An ogre army approaches. Use flags to win the battle!
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        distance = hero.distanceTo(enemy)
        hero.pickUpFlag(flag)
        if distance < 5 and hero.isReady("cleave"):
            hero.cleave(enemy)
    elif enemy:
        hero.attack(enemy)