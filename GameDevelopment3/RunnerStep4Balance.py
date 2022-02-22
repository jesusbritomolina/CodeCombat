# https://codecombat.com/play/level/runner-step-4-balance?
# Step 4 of the Run and Dodge game tutorial.

# GAME PARAMETERS
# Change the game parameters to balance the game.
# How fast static objects move.
GAME_SPEED = 0.5 # ∆
# The player speed.
PLAYER_SPEED = 50 # ∆
# How fast ogres approach the player.
OGRE_SPEED_INC =  0.1 # ∆
# How far from the left side the player is placed.
PLAYER_BASE_X = 15 # ∆
# How many score points for a collected gem.
GEM_SCORE = 5 # ∆
# How many score points for a defeated ogre.
DEFEATED_OGRE_SCORE = 10 # ∆
# The minimum time to survive.
WIN_TIME = 10 # ∆
# The time interval between fences.
FENCE_INTERVAL = 0.5 # ∆
# The time interval between gems.
GEM_INTERVAL = 2 # ∆
# The time interval between ogres.
OGRE_INTERVAL = 2 # ∆


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
    thing.pos.x -= GAME_SPEED
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
game.spawnOgreTime = 1
game.score = 0
game.topScore = db.get("topScore") or 0
ui.track(game, "time")
ui.track(game, "score")
ui.track(game, "topScore")
goal = game.addManualGoal("Survive at least " + WIN_TIME + " seconds.")

# PLAYER
player = game.spawnPlayerXY("captain", PLAYER_BASE_X, 34)
player.maxSpeed = PLAYER_SPEED

def onCollect(event):
    item = event.other
    if item.type == "gem":
        game.score += GEM_SCORE

def onCollide(event):
    unit = event.target
    other = event.other
    if other.type == "fence":
        unit.defeat()

def onDefeatPlayer():
    if game.time > WIN_TIME:
        game.setGoalState(goal, True)
    else:
        game.setGoalState(goal, False)
    setTopScore()

player.on("collect", onCollect)
player.on("collide", onCollide)
player.on("defeat", onDefeatPlayer)

# ENEMIES
def onDefeatOgre(event):
    unit = event.target
    game.score += DEFEATED_OGRE_SCORE
    unit.on("update", onUpdateStatic)

def onUpdateOgre(event):
    unit = event.target
    if unit.health > 0:
        unit.baseX += OGRE_SPEED_INC
        if unit.baseX > PLAYER_BASE_X - 2:
            unit.baseX = PLAYER_BASE_X - 2
        unit.pos.x = unit.baseX


def spawnOgre():
    y = game.randomInteger(12, 56)
    unit = game.spawnXY("scout", 0, y)
    unit.baseX = 0
    unit.on("update", onUpdateOgre)
    unit.on("defeat", onDefeatOgre)
    unit.on("collide", onCollide)
    unit.behavior = "AttacksNearest"

# GAME LOOP
def checkPlayer():
    if game.time == WIN_TIME:
        player.say("Win! Bonus Time!")
    player.pos.x = PLAYER_BASE_X

def setTopScore():
    topScore = db.get("topScore") or 0
    if game.score > game.topScore:
        db.set("topScore", game.score)

def checkSpawns():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += FENCE_INTERVAL
    if game.time > game.spawnGemTime:
        spawnRandomY("gem")
        game.spawnGemTime += GEM_INTERVAL
    if game.time > game.spawnOgreTime:
        spawnOgre()
        game.spawnOgreTime += OGRE_INTERVAL

def onUpdateGame(event):
    checkPlayer()
    checkSpawns()
    game.score += event.deltaTime

game.on("update", onUpdateGame)