# https://codecombat.com/play/level/resource-valleys?
# Collect all the coins!

def commandPeasant(peasant, coins):
    # Find the nearest coin to the `peasant` from the `coins` array,
    item = peasant.findNearest(coins)
    if item:
        hero.command(peasant, "move", item.pos)
    # Command the peasant "move" to the nearest coin.
    pass

friends = hero.findFriends()
peasants = {
    "Aurum": friends[0],
    "Argentum": friends[1],
    "Cuprum": friends[2]
}

while True:
    items = hero.findItems()
    goldCoins = []
    silverCoins = []
    bronzeCoins = []
    for item in items:
        if item.value == 3:
            goldCoins.append(item)
        # Put bronze and silver coins in their approriate array:
        elif item.value == 2:
            silverCoins.append(item)
        elif item.value == 1:
            bronzeCoins.append(item)
    
    commandPeasant(peasants.Aurum, goldCoins)
    commandPeasant(peasants.Argentum, silverCoins)
    commandPeasant(peasants.Cuprum, bronzeCoins)