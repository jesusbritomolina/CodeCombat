# https://codecombat.com/play/level/forest-incursion?
# Okar needs to stomp out these annoying little munchkins!
# Unfortunately he is slow, and his attacks do little damage.
# Fortunately, as a game developer, you have full control over the world!
# Set Okar's properties to buff him up for ogre slaying!
# You can find default values for units on the doc panel.

game.addDefeatGoal()
game.addSurviveGoal()
player = game.spawnPlayerXY("goliath", 12, 10)
# Increase the player's maxSpeed ( > 4), so he runs faster.
player.maxSpeed = 25
# Increase the player's maxHealth ( > 500), so he lasts longer.
player.maxHealth = 510
# Increase the player's attackDamage ( > 7.68), so he can quickly take down the ogres.
player.attackDamage = 7.8