# https://codecombat.com/play/level/game-of-coins-step-2-score?
# Part 2 of creating a Pac-Man style arcade game.
# The game layout and items. Scroll down.
game.spawnXY("forest", 16, 16)
game.spawnXY("forest", 32, 16)
game.spawnXY("forest", 48, 16)
game.spawnXY("forest", 64, 16)
game.spawnXY("forest", 16, 32)
game.spawnXY("forest", 32, 32)
game.spawnXY("forest", 48, 32)
game.spawnXY("forest", 64, 32)
game.spawnXY("forest", 16, 48)
game.spawnXY("forest", 32, 48)
game.spawnXY("forest", 48, 48)
game.spawnXY("forest", 64, 48)

game.spawnXY("bronze-coin", 16, 8)
game.spawnXY("bronze-coin", 24, 8)
game.spawnXY("bronze-coin", 32, 8)
game.spawnXY("bronze-coin", 48, 8)
game.spawnXY("bronze-coin", 56, 8)
game.spawnXY("bronze-coin", 64, 8)
game.spawnXY("bronze-coin", 72, 8)

game.spawnXY("bronze-coin", 8, 16)
game.spawnXY("bronze-coin", 24, 16)
game.spawnXY("bronze-coin", 40, 16)
game.spawnXY("bronze-coin", 56, 16)
game.spawnXY("bronze-coin", 72, 16)

game.spawnXY("bronze-coin", 8, 24)
game.spawnXY("bronze-coin", 16, 24)
game.spawnXY("bronze-coin", 24, 24)
game.spawnXY("bronze-coin", 32, 24)
game.spawnXY("bronze-coin", 40, 24)
game.spawnXY("bronze-coin", 48, 24)
game.spawnXY("bronze-coin", 56, 24)
game.spawnXY("bronze-coin", 64, 24)
game.spawnXY("bronze-coin", 72, 24)

game.spawnXY("bronze-coin", 24, 32)
game.spawnXY("bronze-coin", 56, 32)

game.spawnXY("bronze-coin", 8, 40)
game.spawnXY("bronze-coin", 16, 40)
game.spawnXY("bronze-coin", 24, 40)
game.spawnXY("bronze-coin", 32, 40)
game.spawnXY("bronze-coin", 40, 40)
game.spawnXY("bronze-coin", 48, 40)
game.spawnXY("bronze-coin", 56, 40)
game.spawnXY("bronze-coin", 64, 40)
game.spawnXY("bronze-coin", 72, 40)

game.spawnXY("bronze-coin", 8, 48)
game.spawnXY("bronze-coin", 24, 48)
game.spawnXY("bronze-coin", 40, 48)
game.spawnXY("bronze-coin", 56, 48)
game.spawnXY("bronze-coin", 72, 48)

game.spawnXY("bronze-coin", 8, 56)
game.spawnXY("bronze-coin", 16, 56)
game.spawnXY("bronze-coin", 24, 56)
game.spawnXY("bronze-coin", 32, 56)
game.spawnXY("bronze-coin", 48, 56)
game.spawnXY("bronze-coin", 56, 56)
game.spawnXY("bronze-coin", 64, 56)
game.spawnXY("bronze-coin", 72, 56)

game.spawnXY("mushroom", 40, 8)
game.spawnXY("mushroom", 8, 32)
game.spawnXY("mushroom", 72, 32)
game.spawnXY("mushroom", 40, 56)

# The game score.
game.score = 1000
game.addCollectGoal()
# Setting UI for "score" and "time".
ui.track(game, "time")
ui.track(game, "score")


player = game.spawnPlayerXY("knight", 8, 8)
# High player speed for now, to simplify your level testing.
player.maxSpeed = 30

def onCollect(event):
    player = event.target
    item = event.other
    # If the item's type is "bronze-coin":
    if item.type == "bronze-coin":
        # Increase the game.score by 1.
        game.score += 1
        pass
    # If the type is "mushroom", then increase game.score by 5.
    if item.type == "mushroom":
        game.score +=5

# Assign the event handler on the player's "collect" event.
player.on("collect", onCollect)

# This function reduces the score over time.
def checkTimeScore():
    # Each time frame we reduce the game.score:
    game.score -= 0.5
    # If the game.score is less than 0:
    if game.score < 0:
        # Set the game.score equal to 0:
        game.score = 0

# The main game loop.
while True:
    checkTimeScore()

# Win the game.