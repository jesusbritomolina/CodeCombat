# https://codecombat.com/play/level/center-formation?
# Night is coming! Move all the soldiers towards the fire.

def centerFormation(event):
    # event.target is the unit running this event handler.
    unit = event.target
    # Now use unit.moveXY to move the unit to the fire.
    unit.moveXY(40,36)

# This spawns the four soldiers:
game.spawnXY("soldier", 16, 57)
game.spawnXY("soldier", 15, 13)
game.spawnXY("soldier", 63, 13)
game.spawnXY("soldier", 67, 57)

# This sets the soldier's spawn action to the function centerFormation:
game.setActionFor("soldier", "spawn", centerFormation)