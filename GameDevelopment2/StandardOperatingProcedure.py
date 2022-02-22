# https://codecombat.com/play/level/standard-operating-procedure?
# Events have properties like event.target
# This lets you use the same event handler for many different units.
game.addDefeatGoal()
soldier1 = game.spawnXY("soldier", 50, 30)
soldier2 = game.spawnXY("soldier", 50, 35)
soldier3 = game.spawnXY("soldier", 50, 40)
munchkin1 = game.spawnXY("munchkin", 25, 30)
munchkin2 = game.spawnXY("munchkin", 25, 35)
munchkin3 = game.spawnXY("munchkin", 25, 40)

# This function has munchkin1 attack its enemies.
# Use event.target to make this function work for all units!
def fightEnemies(event):
    while True:
        # Create a unit variable, and assign event.target to it
        unit = event.target
        # Now change the lines below to use unit instead of munchkin1
        enemy = unit.findNearestEnemy() # ∆
        if enemy:
            unit.attack(enemy) # ∆

# Use game.setActionFor() to assign event handlers to many units.
game.setActionFor("munchkin", "spawn", fightEnemies)
game.setActionFor("soldier", "spawn", fightEnemies)