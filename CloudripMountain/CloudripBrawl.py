# https://codecombat.com/play/level/cloudrip-brawl?
# Stay alive for one minute.
# If you win, the next time you play will be more difficult and more rewarding!
# If you lose, you must wait a day before submitting again.

while True:
    item = hero.findNearestItem()
    if (item):
        if (hero.isReady("jump")):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    enemy = hero.findNearestEnemy()
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        while (soldierIndex < len(soldiers)):
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)
            soldierIndex += 1