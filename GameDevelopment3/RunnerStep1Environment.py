# https://codecombat.com/play/level/runner-step-1-environment?
# Step 1 of creating a Run and Dodge game.

# First, spawn the top and bottom forest borders.
game.spawnXY("forest", -4, 64)
game.spawnXY("forest", 4, 64)
game.spawnXY("forest", 12, 64)
game.spawnXY("forest", 20, 64)
game.spawnXY("forest", 28, 64)
game.spawnXY("forest", 36, 64)
game.spawnXY("forest", 44, 64)
game.spawnXY("forest", 52, 64)
game.spawnXY("forest", 60, 64)
game.spawnXY("forest", 68, 64)
game.spawnXY("forest", 76, 64)
game.spawnXY("forest", -4, 4)
game.spawnXY("forest", 4, 4)
game.spawnXY("forest", 12, 4)
game.spawnXY("forest", 20, 4)
game.spawnXY("forest", 28, 4)
game.spawnXY("forest", 36, 4)
game.spawnXY("forest", 44, 4)
game.spawnXY("forest", 52, 4)
game.spawnXY("forest", 60, 4)
game.spawnXY("forest", 68, 4)
game.spawnXY("forest", 76, 4)

# This moves the environment objects to create the illusion of running.
def onUpdateStatic(event):
    thing = event.target
    # Each time frame we move a little to the left:
    thing.pos.x -= 0.8
    # If thing's X coordinate is less than -4:
    if thing.pos.x < -4:
        # If thing's type is "forest":
        if thing.type == "forest":
            # Then set thing.pos.x to 84, so it can re-enter the map from the right side:
            thing.pos.x = 84
        # Otherwise destroy the thing:
        else:
            thing.destroy()

# Assign onUpdateStatic to handle the "update" event for all "forest" objects.
game.setActionFor("forest", "update", onUpdateStatic)

# This spawns a fence on the right side of the map, at a random Y coordinate.
def spawnRandomY(type):
    y = game.randomInteger(12, 56)
    spawn = game.spawnXY(type, 80, y)
    # Fences should move to the left.
    spawn.on("update", onUpdateStatic)

# This spawns a number of fences, based on the game time.
def spawnFences():
    # Spawn 1 until 10 seconds, 2 until 20 seconds, and so on.
    spawnNumber = 1 + (game.time / 10)
    while spawnNumber >= 1:
        spawnRandomY("fence")
        spawnNumber -= 1

# Setup the game, timers, UI, and goals.
game.spawnFenceTime = 0
ui.track(game, "time")
game.addSurviveGoal(15)

# Player setup.
player = game.spawnPlayerXY("captain", 12, 34)
player.maxSpeed = 20

# This handles the player's "collide" events. Defeat the player if they hit a fence!
def onCollide(event):
    unit = event.target
    other = event.other
    if other.type == "fence":
        unit.defeat()

player.on("collide", onCollide)

# Those functions define the game loop.
def checkPlayer():
    # The player should be stationary along the X axis, so we set their X position to a constant number.
    player.pos.x = 20

def checkTimers():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += 1

def onUpdateGame(event):
    checkPlayer()
    checkTimers()

game.on("update", onUpdateGame)