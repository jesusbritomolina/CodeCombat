# https://codecombat.com/play/level/the-dunes?
# Collect coins. Ignore "sand-yak"s and "burl"s.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if enemy.type == "sand-yak" or enemy.type == "burl":
            # Don't attack! Collect coins.
            hero.moveXY(item.pos.x,item.pos.y)
            pass
        else:
            # Else, attack.
            hero.attack(enemy)
            pass
        
    elif item:
        # Collect coins: move to item's position.
        hero.moveXY(item.pos.x,item.pos.y)
        pass
    else:
        hero.moveXY(41, 31)