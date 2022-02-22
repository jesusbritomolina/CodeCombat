# https://codecombat.com/play/level/defend-the-garrison?
# Defeat all of the attacking ogres.
# Use flags to move away from dangerous ogres.

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