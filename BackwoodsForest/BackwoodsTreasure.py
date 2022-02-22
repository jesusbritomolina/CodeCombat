# https://codecombat.com/play/level/backwoods-treasure?
# Collect 100 gold from two or three groves.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    item = hero.findNearestItem()
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        hero.attack(enemy)
    elif item:
        hero.moveXY(item.pos.x, item.pos.y)