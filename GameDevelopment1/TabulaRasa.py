# https://codecombat.com/play/level/tabula-rasa?
# Create your own game!

# Spawn a player with spawnPlayerXY(type, x, y)
player = game.spawnPlayerXY("captain", 36, 30)
# Add at least one goal!
game.addDefeatGoal()
# Spawn objects into the game with spawnXY(type, x, y)
game.spawnXY("fence", 16, 30)