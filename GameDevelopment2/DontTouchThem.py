# https://codecombat.com/play/level/dont-touch-them?
# Use manual goals to specify which ogres to defeat.

def createGenerator(spawnType, x, y, spawnAI):
    generator = game.spawnXY("generator", x, y)
    generator.spawnType = spawnType
    generator.spawnAI = spawnAI

# Scouts are aggressive and munchkins are just walking.
createGenerator("scout", 12, 12, "AttacksNearest")
createGenerator("scout", 68, 56, "AttacksNearest")
createGenerator("munchkin", 12, 56, "Scampers")
createGenerator("munchkin", 68, 12, "Scampers")

player = game.spawnPlayerXY("duelist", 40, 34)
player.maxHealth = 1000
player.attackDamage = 20
player.maxSpeed = 20

# These are our goals. Notice we save them in variables!
spawnMunchkinsGoal = game.addManualGoal("Let 6 munchkins spawn.")
dontTouchGoal = game.addManualGoal("Don't attack munchkins.")
defeatScoutsGoal = game.addManualGoal("Defeat 6 scouts.")
# game properties used to count new and defeated ogres.
game.spawnedMunchkins = 0
game.defeatedScouts = 0
ui.track(game, "spawnedMunchkins")
ui.track(game, "defeatedScouts")

def onSpawn(event):
    game.spawnedMunchkins += 1

def onDefeat(event):
    unit = event.target
    if unit.type == "scout":
        game.defeatedScouts += 1
    if unit.type == "munchkin":
        # dontTouchGoal is failed if a munchkin is defeated.
        game.setGoalState(dontTouchGoal, False)
        player.say("Oops.")

def checkGoals():
    # If game.defeatedScouts is greater than 5:
    if game.defeatedScouts > 5:
        # Set defeatScoutsGoal state as successful..
        game.setGoalState(defeatScoutsGoal, True)
    # If game.spawnedMunchkins is greater than 5:
    if game.spawnedMunchkins > 5:
        # Set spawnMunchkinsGoal state as successful..
        game.setGoalState(spawnMunchkinsGoal, True)
    # If both other goals are completed.
    if spawnMunchkinsGoal.success:
        if defeatScoutsGoal.success:
            # Set dontTouchGoal state as successful..
            game.setGoalState(dontTouchGoal, True)

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("munchkin", "defeat", onDefeat)
game.setActionFor("scout", "defeat", onDefeat)

while True:
    checkGoals()