# https://codecombat.com/play/level/lernaean-hydra?
# For each defeated ogre, spawn two new ogres.

player = game.spawnPlayerXY("knight", 40, 34)
player.attackDamage = 20

# Use this to count defeated ogres.
game.defeated = 0
# How many ogres the player needs to defeat
game.toDefeat = 16
game.addDefeatGoal(game.toDefeat)
# Show these useful variables to the player using ui.track
ui.track(player, "health")
ui.track(game, "defeated")
ui.track(game, "toDefeat")

# Starter enemies.
game.spawnXY("munchkin", 30, 14)
game.spawnXY("munchkin", 50, 54)

# This makes new enemies aggresive.
def onSpawn(event):
    unit = event.target
    unit.behavior = "AttacksNearest"

# Count defeated enemies and spawn new ones.
def onDefeat(event):
    unit = event.target
    # Decrease the game's toDefeat property.
    game.toDefeat -= 1
    # Increase the game's defeated property:
    game.defeated += 1
    # Get random coordinates for new enemies.
    x1 = game.randomInteger(10, 40)
    x2 = game.randomInteger(40, 70)
    y = game.randomInteger(12, 56)
    game.spawnXY("potion-small", unit.pos.x, unit.pos.y)
    # Spawn a "munchkin" at the point x1, y:
    game.spawnXY("munchkin", x1, y)
    # Spawn a "munchkin" at the point x2, y:
    game.spawnXY("munchkin", x2, y)

game.setActionFor("munchkin", "spawn", onSpawn)
# Set "munchkin"s "defeat" event handler to onDefeat:
game.setActionFor("munchkin", "defeat", onDefeat)