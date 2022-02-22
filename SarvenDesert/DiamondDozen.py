# https://codecombat.com/play/level/diamond-dozen?
# Claim the coins while defeating the marauding ogres.

def findMostHealth(enemies):
    target = None
    targetHealth = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
        enemyIndex += 1
    return target

def valueOverDistance(item):
    return item.value / hero.distanceTo(item)

# Return the item with the highest valueOverDistance(item)
def findBestItem(items):
    bestItem = None
    bestValue = 0
    itemsIndex = 0
    
    # Loop over the items array.
    # Find the item with the highest valueOverDistance()
    while itemsIndex < len(items):
        item = items[itemsIndex]
        itemsIndex += 1
        if valueOverDistance(item) > bestValue:
            bestValue = valueOverDistance(item)
            bestItem = item
    return bestItem

while True:
    enemies = hero.findEnemies()
    enemy = findMostHealth(enemies)
    if enemy and enemy.health > 15:
        while enemy.health > 0:
            hero.attack(enemy)
    else:
        coins = hero.findItems()
        coin = None
        coin = findBestItem(coins)
        if coin:
            hero.moveXY(coin.pos.x, coin.pos.y)