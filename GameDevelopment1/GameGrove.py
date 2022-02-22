# https://codecombat.com/play/level/game-grove?
# Make your own game by changing the code below!
# Spawn a maze. Change the number for a different maze!
game.spawnMaze(1)

# Spawn a player with spawnPlayerXY()
player = game.spawnPlayerXY("raider", 28, 60)
player.attackDamage = 10
player.maxHealth = 200

# Add at least one goal!
game.addCollectGoal()
game.addSurviveGoal()

# Spawn some things to collect!
game.spawnXY("gem", 28, 27)
# You need a key to collect a locked chest.
game.spawnXY("locked-chest", 44, 28)
game.spawnXY("silver-key", 43, 60)
game.spawnXY("potion-medium", 60, 12)

# Spawn some enemies!
s1 = game.spawnXY("skeleton", 43, 50)
s1.behavior = "Defends"
s2 = game.spawnXY("skeleton", 49, 59)
s2.behavior = "Defends"
game.spawnXY("lightstone", 60, 44)

gen = game.spawnXY("generator", 26, 44)
gen.spawnType = "munchkin"
gen.spawnDelay = 4

game.spawnXY("munchkin", 28, 19)
# Ogre Spear Throwers have a ranged attack!
game.spawnXY("thrower", 48, 28)
# This gargoyle shoots fire!
spewer = game.spawnXY("fire-spewer", 37, 12)
spewer.direction = "horizontal"

# Track plays and ogres defeated in the database.
db.add("plays", 1)
ui.track(db, "plays")
ui.track(db, "defeated")

def onVictory(event):
    db.add("defeated", game.defeated)

game.on("victory", onVictory)