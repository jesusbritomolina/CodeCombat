# https://codecombat.com/play/level/army-training-2?
# Defeat the ogres using event handlers to command units.

# Spawn 2 "soldier"s.
game.spawnXY("soldier", 35, 20)
game.spawnXY("soldier", 45, 20)
# Spawn 2 "archer"s.
game.spawnXY("archer", 25, 20)
game.spawnXY("archer", 55, 20)
def fightEnemies(event):
    while True:
        # event.target is the unit that is executing this event handler function!
        friendUnit = event.target
        enemy = friendUnit.findNearestEnemy()
        # Have friendUnit attack() the enemy!
        friendUnit.attack(enemy)

# This attaches the fightEnemies handler to all soldiers' "spawn" events.
game.setActionFor("soldier", "spawn", fightEnemies)

# Now, attach fightEnemies to the archers' "spawn" events:
game.setActionFor("archer", "spawn", fightEnemies)