# https://codecombat.com/play/level/disintegration-arrow?
# Destroy at least 50 defeated ogres.

# This spawns and configures an archer.
def spawnArcher(x, y):
    archer = game.spawnXY("archer", x, y)
    archer.behavior = "Defends"
    archer.attackDamage = 20

# This spawns and configures an ogre.
def spawnMunchkin(x, y):
    ogre = game.spawnXY("munchkin", x, y)
    ogre.behavior = "AttacksNearest"

# Spawns some archers in a row.
def spawnArcherWall():
    spawnArcher(30, 12)
    spawnArcher(30, 23)
    spawnArcher(30, 34)
    spawnArcher(30, 45)
    spawnArcher(30, 56)

# Spawns an ogre wave with a random offset for variety.
def spawnOgreWave():
    offset = game.randomInteger(-6, 6)
    spawnMunchkin(80, 16 + offset)
    spawnMunchkin(80, 22 + offset)
    spawnMunchkin(80, 28 + offset)
    spawnMunchkin(80, 34 + offset)
    spawnMunchkin(80, 40 + offset)
    spawnMunchkin(80, 46 + offset)
    spawnMunchkin(80, 52 + offset)


def onDefeat(event):
    unit = event.target
    # Increase the game.defeated counter by 1.
    game.defeated += 1
    # Use unit.destroy() to destroy it.
    unit.destroy()
    

# Set "munchkin"s "defeat" event handlers to onDefeat.
game.setActionFor("munchkin", "defeat", onDefeat)

game.defeated = 0
game.spawnTime = 0
# Add a manual goal.
goal = game.addManualGoal("Defeat 77 ogres.")
ui.track(game, "defeated")

def checkSpawnTimer():
    if game.time > game.spawnTime:
        spawnOgreWave()
        game.spawnTime += 1

def checkGoal():
    # If the game.defeated counter is greater than 77:
    if game.defeated > 77:
        # Set the goal as successfully completed.
        game.setGoalState(goal, True)
    pass

spawnArcherWall()
while True:
    checkSpawnTimer()
    checkGoal()