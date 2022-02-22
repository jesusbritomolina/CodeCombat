# https://codecombat.com/play/level/timber-turncoat?
while True:
    # Collect gold.
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    # If you have enough gold, summon a soldier.
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
    elif hero.isReady("summon-burl"):
        hero.cast("summon-burl")
    # Use a for-loop to command each soldier.
    for friend in hero.findFriends():
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            # If there's an enemy, command her to attack.
            # Careful! If your soldiers are defeated, a warlock will appear!
            # Otherwise, move her to the right side of the map.
            if enemy:
                hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {'x':77,'y':43})
            if friend.health <= 20:
                hero.command(friend, "move", hero.pos)