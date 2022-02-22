# https://codecombat.com/play/level/backwoods-brawl?
# Stay alive for one minute.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        hero.attack(enemy)