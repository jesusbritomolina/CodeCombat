# https://codecombat.com/play/level/from-dust-to-dust?
# Block passages with forest tiles.
# Then destroy them when the player defeats some ogres.

# Set up the player.
player = game.spawnPlayerXY("duelist", 6, 34)
player.attackDamage = 35
player.maxHealth = 750
player.maxSpeed = 15
# The player should move through the forest to win.
game.addMoveGoalXY(76, 34)

# Set up enemies.
munchkinSpawner = game.spawnXY("generator", 16, 56)
munchkinSpawner.spawnType = "munchkin"
munchkinSpawner.spawnDelay = 3
scoutSpawner = game.spawnXY("generator", 40, 10)
scoutSpawner.spawnType = "scout"
scoutSpawner.spawnDelay = 5

# These forest tiles should block the passages.
passageForest1 = game.spawnXY("forest", 28, 34)
# Create the second forest to block the second passage {52, 34}:
passageForest2 = game.spawnXY("forest", 52, 34)

game.defeated = 0
ui.track(game, "defeated")

def onDefeat(event):
    defeated = event.target
    game.defeated += 1
    # If 3 ogres are defeated:
    if game.defeated == 3:
        # Defeat the munchkinSpawner.
        munchkinSpawner.defeat()
        # Destroy the first forest passage.
        passageForest1.destroy()
    # If 6 ogres are defeated:
    if game.defeated == 6:
        # Call the defeat method for the scoutSpawner:
        scoutSpawner.defeat()
        # Destroy the second forest passage.
        passageForest2.destroy()
# Set the "defeat" event handler for "munchkin"s and "scout"s.
game.setActionFor("munchkin", "defeat", onDefeat)
game.setActionFor("scout", "defeat", onDefeat)


# Beat the game!