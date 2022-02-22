# https://codecombat.com/play/level/sarven-brawl?
# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy and enemy.type != "sand-yak":
        if hero.isReady("power-up"):
            hero.powerUp()
        else:
            hero.attack(enemy)
    else:
        hero.moveXY(28, 68)