# https://codecombat.com/play/level/seeing-is-believing?
# Players like seeing score, so use ui.track()!
# It will create a user-interface element for them to see.
player = game.spawnPlayerXY("samurai", 20, 20)

game.addSurviveGoal(20)

spawner = game.spawnXY("generator", 50, 50)
spawner.maxHealth = 9001
spawner.spawnType = "munchkin"
# Add more spawners for more enemies on the field:
spawner.spawnType = "munchkin"
game.spawnXY("generator", 21, 20)

# ui.track() displays an object's property for players to see!
ui.track(game, "time")
# Use ui.track to track game's "defeated" property:
ui.track(game, "defeated")
player.attackDamage = 1000
# Increase the hero's maxSpeed:
player.maxSpeed = 10
# Press play and defeat 6 munchkins or skeletons!