# https://codecombat.com/play/level/mad-maxer-gets-greedy?
# aaaaaaaaaaaaaaaa
# aaaaaaaaaaaa
while True:
    bestCoin = None
    maxRating = 0
    coinIndex = 0
    coins = hero.findItems()
    # aaaaaaaaaaaaaaaaaa
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        if coin.value / distance > maxRating:
            bestCoin = coin
            maxRating = coin.value / distance
            
    if bestCoin:
        hero.moveXY(bestCoin.pos.x, bestCoin.pos.y)