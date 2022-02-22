# https://codecombat.com/play/level/mad-maxer-sells-out?
# Coins here disappear after a few seconds!
# Get all the gold coins before they vanish.

while True:
    closestGold = None
    minGoldDist = 9001
    coinIndex = 0
    coins = hero.findItems()
    # Find the closest coin that is gold.
    # Remember that gold coins have a value of 3.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        if coin.value == 3 and distance < minGoldDist:
            closestGold = coin
            minGoldDist = distance
    if closestGold:
        #Now go to the closest gold coin and get it!
        hero.moveXY(closestGold.pos.x, closestGold.pos.y)
        pass