# https://codecombat.com/play/level/hedge-magic?
# Spawn a maze. Change the number for a different maze!
game.spawnMaze("forest", 1)

# Spawn a hero with spawnPlayerXY(type, x, y)
player = game.spawnPlayerXY("captain", 36, 30)
# Add at least one goal!
game.addDefeatGoal()