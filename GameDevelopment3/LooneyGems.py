# https://codecombat.com/play/level/looney-gems?
#  Why should gems wait while you are collecting them?

# This spawns a gem at a random point with random directions
def spawnRandomGem():
    x = game.randomInteger(10, 70)
    y = game.randomInteger(10, 58)
    gem = game.spawnXY("gem", x, y)
    # This defines the direction along the X axis. 1 means move to the right. -1 means move to the left. Zero means don't move horizontally.
    gem.dirX = game.randomInteger(-1, 1)
    # This defines the direction along the Y axis. 1 means move up, -1 means move down. Zero means don't move vertically.
    gem.dirY = game.randomInteger(-1, 1)
    gem.scale = 1.5

# Spawn as many gems as you want.
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()

gemSpeed = 0.6

# This handler moves gems.
def onUpdate(event):
    item = event.target
    # There are two parts of moving: X and Y.
    diffX = item.dirX * gemSpeed
    diffY = item.dirY * gemSpeed
    # Increase item.pos.x by diffX:
    item.pos.x += diffX
    # Increase item.pos.y by diffY:
    item.pos.y += diffY
    # If the item is out of bounds for the X coordinate
    if item.pos.x > 70 or item.pos.x < 10:
        # Multiply item.dirX by -1 to flip the X direction:
        item.dirX *= -1
    # If item.pos.y is greater than 58 or less than 10:
    if item.pos.y > 58 or item.pos.y < 10:
        # Multiply item.dirY by -1 to flip the Y direction:
        item.dirY *= -1

game.setActionFor("gem", "update", onUpdate)

player = game.spawnPlayerXY("captain", 40, 34)
player.maxSpeed = 20
game.addCollectGoal()
ui.track(game, "time")