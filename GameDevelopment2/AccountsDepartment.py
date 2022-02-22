# https://codecombat.com/play/level/accounts-department?
# Count collected item values and use them for scoring.

# Setup characters.
player = game.spawnPlayerXY("captain", 40, 34)
player.maxSpeed = 20

# Chests of gems are the most valuable items.
game.spawnXY("chest", 68, 56)
game.spawnXY("chest", 14, 14)

# This function spawns a random item in a random place.
def spawnRandomItem():
    itemNumber = game.randomInteger(1, 3)
    x = game.randomInteger(12, 68)
    y = game.randomInteger(12, 56)
    if itemNumber == 1:
        game.spawnXY("bronze-coin", x, y)
    elif itemNumber == 2:
        game.spawnXY("gold-coin", x, y)
    elif itemNumber == 3:
        game.spawnXY("gem", x, y)

itemInterval = 1
itemSpawnTime = 0

def checkSpawnTimer():
    if game.time >= itemSpawnTime:
        # Call the spawnRandomItem function.
        spawnRandomItem()
        itemSpawnTime += itemInterval

game.score = 0

# The "collect" event is triggered by collecting something.
def onCollect(event):
    # event.target contains the collector.
    collector = event.target
    # event.other contains the collected item.
    item = event.other
    if item.value:
        # Adding health power for valuable items.
        collector.health += item.value
        # Increase the game score by the item's `value`:
        game.score += item.value
        pass

# Asignar onCollect handler para "héroe" en evento "collect".
player.on("collect", onCollect)

# The score the player needs to win.
requiredScore = 220
goldGoal = game.addManualGoal('Recoge al menos 220 de oro en 20 segundos.')
ui.track(game, "score")

def checkGoals():
    if game.score >= requiredScore:
        game.setGoalState(goldGoal, True)

while True:
    checkSpawnTimer()
    checkGoals()