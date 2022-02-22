# https://codecombat.com/play/level/chokepoint?
# Ogres are advancing through the forest lanes!
# Spawn some soldiers and have them defend their lanes!

def defendLane(event):
    # Remember to create a variable for the target, to remember:
    unit = event.target
    # Save the unit's starting pos.x
    startX = unit.pos.x
    while True:
        enemy = unit.findNearestEnemy()
        # If there is an enemy.
        if enemy:
            # Use unit.attack to attack the enemy:
            unit.attack(enemy)
            pass
        else:
            # Move the unit back to it's starting x and y.
            unit.moveXY(startX, 16)
        

game.spawnXY("soldier", 9, 16)
game.spawnXY("soldier", 30, 16)
game.spawnXY("soldier", 54, 16)
game.spawnXY("soldier", 75, 16)

# Set the event handler defendLane on "spawn" event for "soldier"s.
game.setActionFor("soldier", "spawn", defendLane);