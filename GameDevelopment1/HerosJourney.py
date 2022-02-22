# https://codecombat.com/play/level/heros-journey?
# Each game must have a player and a goal.

# Use game.spawnPlayerXY("captain", x, y)
# to add a player to your game:
player = game.spawnPlayerXY("captain", 16, 30)
# Use game.addMoveGoalXY(x, y)
# to add a movement goal to your game:
# it should be 10m away from the player.
game.addMoveGoalXY(36, 30)
# If you want to, use spawnXY("fence", x, y)
# to make a maze with fences...
game.spawnXY("fence", 26, 30)
# Then, click "Test Level" to try your first playable game!