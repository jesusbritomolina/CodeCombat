# https://codecombat.com/play/level/runner-step-2-scoring?
# Step 2 of the Run and Dodge game tutorial.

# ENVIROMENT
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

def onUpdateStatic(event):
    thing = event.target
    thing.pos.x -= 0.6
    if thing.pos.x < -4:
        if thing.type == "forest":
            thing.pos.x = 84
        else:
            thing.destroy()

game.setActionFor("forest", "update", onUpdateStatic)

def spawnRandomY(type):
    y = game.randomInteger(12, 56)
    spawn = game.spawnXY(type, 80, y)
    spawn.on("update", onUpdateStatic)

def spawnFences():
    spawnNumber = 1 + (game.time / 10)
    while spawnNumber >= 1:
        spawnRandomY("fence")
        spawnNumber -= 1

# GAME SETTINGS
# One timer for fence spawning, and another for gems.
game.spawnFenceTime = 0
game.spawnGemTime = 0.5
# We use game.score to track the current score.
game.score = 0
# Get the previous top score from the db.
game.topScore = db.get("topScore") or 0
ui.track(game, "time")
ui.track(game, "score")
ui.track(game, "topScore")
# Use a manual goal so we can count it as a win but let the game continue.
goal = game.addManualGoal("Survive at least 20 seconds.")

# PLAYER
player = game.spawnPlayerXY("captain", 20, 34)
player.maxSpeed = 20

# This handles "collect" events for scoring gems.
def onCollect(event):
    item = event.other
    # If the item's type is "gem":
    if item.type == "gem":
        # Increase game.score by some value:
        game.score += 1

# This handles the game over state when the player is defeated.
def onDefeatPlayer(event):
    # game.setGoalState(goal, false)
    # If game.time is greater than 20:
    if game.time > 20:
        # Set the goal state to True.
        game.setGoalState(goal, True)
    # Otherwise:
    else:
        # Set the goal state to False.
        e.setGoalState(goal, false)
    setTopScore()

# This handles collisions. Defeat the player if they hit a fence.
def onCollide(event):
    unit = event.target
    other = event.other
    if other.type == "fence":
        unit.defeat()

player.on("collect", onCollect)
player.on("collide", onCollide)
player.on("defeat", onDefeatPlayer)

# GAME LOOP
# This checks the player's health and position.
def checkPlayer():
    if game.time == 20:
        player.say("Win! Bonus time!")
    player.pos.x = 20

# This sets the top score.
def setTopScore():
    game.topScore = db.get("topScore") or 0
    if game.score > game.topScore:
        db.set("topScore", game.score)

# This checks timers for gems and fences.
def checkSpawns():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += 1
    if game.time > game.spawnGemTime:
        spawnRandomY("gem")
        game.spawnGemTime += 1

def onUpdateGame(event):
    checkPlayer()
    checkSpawns()
    # Score increases with the game time. event.deltaTime is the amount of time since the last "update" happened.
    game.score += event.deltaTime

game.on("update", onUpdateGame)