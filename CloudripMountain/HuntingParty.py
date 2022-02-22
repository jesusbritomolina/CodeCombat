# https://codecombat.com/play/level/hunting-party?
# You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours.
while True:
    friends = hero.findFriends()
    # Use for-loop and for each friend:
    for friend in friends:
        # If they see an enemy then command to attack.
        enemy = friend.findNearestEnemy()
        if friend.health < 100 and friend.type == "soldier" or friend.health < 15 and friend.type == "archer":
            hero.command(friend, "move", {'x':friend.pos.x-1,'y':friend.pos.y})
        elif enemy:
            hero.command(friend, "attack", enemy)
        # Command to move east by small steps.
        else:
            hero.command(friend, "move", {'x':friend.pos.x+0.3,'y':friend.pos.y})