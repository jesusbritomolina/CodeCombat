# https://codecombat.com/play/level/sarven-treasure?
# Collect 150 gold while evading ogres with teleporters.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    enemys = hero.findEnemies()
    items = hero.findItems()
    item = hero.findNearest(items)
    enemy = hero.findNearest(enemys)
    if (enemy and hero.distanceTo(enemy) < 15):
        hero.attack(enemy)
    elif (item):
        if (hero.isReady('jump')):
            hero.jumpTo(item.pos)
        else:
            hero.move(item.pos)