# https://codecombat.com/play/level/time-to-live?
# Pass an argument to addSurviveGoal() to specify a time.


# This means the player must survive for 20 seconds.
game.addSurviveGoal(20)

# Spawn a generator with spawnXY
# Use the variable to configure the generator below.
generator = game.spawnXY("generator", 60, 40)
# Set the generator's spawnType to "munchkin"
generator.spawnType = "munchkin"

# Use spawnPlayerXY to spawn a hero for the player.
player = game.spawnPlayerXY("knight", 15, 15)
# Set the player's maxHealth to at least 100
player.maxHealth = 1000
# Set the player's attackDamage to at least 10
player.attackDamage = 200

# Play the game!