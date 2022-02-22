# https://codecombat.com/play/level/timber-guard?
while True:
    # Collect gold.
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    # If you have enough gold, summon a soldier.
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
    # Use a for-loop to command each soldier.
    # For loops have two parts: "for X in Y"
    # Y is the array to loop over.
    # The loop will run once for each item in Y, with X set to the current item.
    for friend in hero.findFriends():
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            # If there's an enemy, command her to attack.
            # Otherwise, move her to the right side of the map.
            if enemy:
                hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {'x':80,'y':45})