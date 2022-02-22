# https://codecombat.com/play/level/runner-step-3-enemies?
# Step 3 of the Run and Dodge game tutorial.

# ENVIRONMENT
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
game.spawnFenceTime = 0
game.spawnGemTime = 0.5
# One more spawn timer, for ogres.
game.spawnOgreTime = 1
game.score = 0
game.topScore = db.get("topScore") or 0
ui.track(game, "time")
ui.track(game, "score")
ui.track(game, "topScore")
goal = game.addManualGoal("Survive at least 20 seconds.")

# PLAYER
player = game.spawnPlayerXY("captain", 20, 34)
player.maxSpeed = 20

def onCollect(event):
    item = event.other
    if item.type == "gem":
        game.score += 5

def onCollide(event):
    unit = event.target
    other = event.other
    if other.type == "fence":
        unit.defeat()

def onDefeatPlayer():
    if game.time > 20:
        game.setGoalState(goal, True)
    else:
        game.setGoalState(goal, False)
    setTopScore()

player.on("collect", onCollect)
player.on("collide", onCollide)
player.on("defeat", onDefeatPlayer)

# ENEMIES
# This handles defeated ogres.
def onDefeatOgre(event):
    unit = event.target
    game.score += 10
    # Defeated ogres should move to the left, just like other environmental objects.
    unit.on("update", onUpdateStatic)

# This updates the positions of the ogres so they slowly catch up to the player.
def onUpdateOgre(event):
    unit = event.target
    # Only update position for un-defeated ogres, who have positive health.
    if unit.health > 0:
        # Set the unit closer to the player. We use the baseX property to track this, because the default ogre behavior might also change it's pos.x property, so we can't use that directly.
        unit.baseX += 0.1
        # If unit.baseX greater than 18:
        if unit.baseX > 18:
            # Set unit.baseX to 18:
            unit.baseX = 18
        # Set unit.pos.x to unit.baseX:
        unit.pos.x = unit.baseX


def spawnOgre():
    y = game.randomInteger(12, 56)
    unit = game.spawnXY("scout", 0, y)
    unit.baseX = 0
    # Assign onUpdateOgre to handle the "update" event on unit:
    unit.on("update", onUpdateOgre)
    # Assign onDefeatOgre to handle the "defeat" event on unit:
    unit.on("defeat", onDefeatOgre)
    unit.on("collide", onCollide)
    unit.behavior = "AttacksNearest"

# GAME LOOP
def checkPlayer():
    if game.time == 20:
        player.say("Win! Bonus time!")
    player.pos.x = 20

def setTopScore():
    topScore = db.get("topScore") or 0
    if game.score > game.topScore:
        db.set("topScore", game.score)

def checkSpawns():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += 1
    if game.time > game.spawnGemTime:
        spawnRandomY("gem")
        game.spawnGemTime += 1
    if game.time > game.spawnOgreTime:
        spawnOgre()
        game.spawnOgreTime += 2

def onUpdateGame(event):
    checkPlayer()
    checkSpawns()
    game.score += event.deltaTime

game.on("update", onUpdateGame)