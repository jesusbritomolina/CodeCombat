# https://codecombat.com/play/level/vorpal-mouse?
# When playing, click an ogre to attack!
# No need to type any code for this level, just click Test Level!

# The following code spawns a playable hero:
game.spawnPlayerXY("guardian", 40, 40)

# These add goals to the level:
game.addDefeatGoal()
game.addSurviveGoal()

# This spawns some enemies to fight:
game.spawnXY("munchkin", 40, 25)
game.spawnXY("munchkin", 15, 15)
game.spawnXY("munchkin", 65, 15)

# This spawns a maze for the player:
game.spawnXY("forest", 30, 54)
game.spawnXY("forest", 50, 54)
game.spawnXY("forest", 30, 48)
game.spawnXY("forest", 50, 48)
game.spawnXY("forest", 30, 40)
game.spawnXY("forest", 50, 40)
game.spawnXY("forest", 30, 32)
game.spawnXY("forest", 50, 32)
game.spawnXY("forest", 30, 26)
game.spawnXY("forest", 50, 26)
game.spawnXY("forest", 30, 10)
game.spawnXY("forest", 50, 10)
game.spawnXY("forest", 22, 26)
game.spawnXY("forest", 58, 26)
game.spawnXY("forest", 14, 26)
game.spawnXY("forest", 66, 26)