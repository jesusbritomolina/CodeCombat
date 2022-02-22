# https://codecombat.com/play/level/mega-munchkin-attacks?
# That's a big'un! With some clever thinking, Ivy should be able to take care of this situation single-handedly.
while True:
    # Find the archer.
    friend = hero.findNearest(hero.findFriends())
    enemy = hero.findNearest(hero.findEnemies())
    
    # Tell the archer to attack the enemy!
    if friend and enemy:
        hero.command(friend, "attack", enemy)
        distance = friend.distanceTo(enemy)
    
    # Wait, no, that doesn't work that well. Maybe try something else?
    # The munchkin is awfully slow...
    if distance < 10:
        hero.command(friend, "move", {'x':15,'y':13})