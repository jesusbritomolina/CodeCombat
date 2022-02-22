# https://codecombat.com/play/level/multiplayer-treasure-grove?
# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.

while True:
    #  Find coins and/or attack the enemy.
    # Use flags and your special moves to win!
    item = hero.findNearestItem()
    flag = hero.findFlag()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    elif flag:
        hero.pickUpFlag(flag)