# https://codecombat.com/play/level/crushing-it?
# If you forget any commands, look to the left of the code window!

# Spawn a hero using game.spawnPlayerXY(type, x, y).
player = game.spawnPlayerXY("captain", 36, 30)
game.addSurviveGoal()
# Add a goal to defeat ogres with game.addDefeatGoal()
game.addDefeatGoal()

game.spawnXY("munchkin", 40, 10)
# Spawn at least 3 more munchkins.
game.spawnXY("munchkin", 56, 30)
game.spawnXY("munchkin", 40, 50)
game.spawnXY("munchkin", 70, 50)