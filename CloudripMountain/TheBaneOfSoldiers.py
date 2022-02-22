# https://codecombat.com/play/level/the-bane-of-soldiers?
# Robobombs explode when they are destroyed or touch an enemy.
# Split up your soldiers so that they don't all get exploded together.

while True:
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    friends = hero.findFriends()
    # Send the first soldier of the friends array towards the enemy.
    firstfriend = friends[0]
    for enemy in enemies:
        for friend in friends:
            hero.command(firstfriend, "attack", enemy)
    # i in range(1, n) starts the index at the second element!
    for i in range(1, len(friends)):
        friend = friends[i]
        # Command the remaining soldiers to run away!
        hero.command(friend, "move", {'x':15,'y':30})