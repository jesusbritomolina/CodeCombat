# https://codecombat.com/play/level/cages?
# Aprende la diferencia entre destroy y defeat.

# generador de enemigos
ogre1 = game.spawnXY("ogre", 12, 18)
ogre1.behavior = "AttacksNearest"
ogre2 = game.spawnXY("ogre", 68, 50)
ogre2.behavior = "AttacksNearest"

munchkinGenerator = game.spawnXY("generator", 12, 50)
munchkinGenerator.spawnAI = "Scampers"
munchkinGenerator.spawnType = "munchkin"

scoutGenerator = game.spawnXY("generator", 68, 12)
scoutGenerator.spawnAI = "Scampers"
scoutGenerator.spawnType = "scout"

# Las vallas que destruirá más tarde.
leftFence = game.spawnXY("fence", 26, 14)
rightFence = game.spawnXY("fence", 54 , 50)

player = game.spawnPlayerXY("knight", 40, 34)
player.maxSpeed = 16
player.attackDamage = 20

# Los contadores globales del juego.
game.scoutsSpawned = 0
game.munchkinsSpawned = 0
game.bossesDefeated = 0
ui.track(game, "scoutsSpawned")
ui.track(game, "munchkinsSpawned")
ui.track(game, "bossesDefeated")

bossesGoal = game.addManualGoal("derrota 2 ogros grandes.")

def onSpawn(event):
    unit = event.target
    if unit.type == "scout":
        game.scoutsSpawned += 1
    if game.scoutsSpawned >= 3:
        # Derrota el generador scout (scoutGenerator) con el método defeat().
        scoutGenerator.defeat()
        # Destruye la vall derecha (rightFence) con el método destroy().
        rightFence.destroy()
        pass
    if unit.type == "munchkin":
        game.munchkinsSpawned += 1
    if game.munchkinsSpawned >= 2:
        # Derrota el generador Munchkin (munchkinGenerator).
        munchkinGenerator.defeat()
        # Destruye la valla izquierda (leftFence)
        leftFence.destroy()
        pass

def onDefeat(event):
    unit = event.target
    if unit.type == "ogre":
        # Incrementa el contador game.bossesDefeated en 1:
        game.bossesDefeated += 1

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("scout", "spawn", onSpawn)
game.setActionFor("ogre", "defeat", onDefeat)

while True:
    if game.bossesDefeated >= 2:
        game.setGoalState(bossesGoal, True)