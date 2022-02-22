# https://codecombat.com/play/level/give-and-take?
# Move to all the X-marks.
# Those fire-traps hurt!

game.spawnPlayerXY("samurai", 40, 50)
game.addSurviveGoal()
game.addMoveGoalXY(25,40)
game.spawnXY("fire-trap", 25, 40)
game.addMoveGoalXY(55,40)
game.spawnXY("fire-trap", 55, 40)
game.addMoveGoalXY(40,20)
game.spawnXY("fire-trap", 40, 20)

# Spawn some "potion-small" objects to heal the player!
game.spawnXY("potion-small", 36, 30)
game.spawnXY("potion-small", 46, 30)