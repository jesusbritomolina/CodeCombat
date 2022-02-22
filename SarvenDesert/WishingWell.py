# https://codecombat.com/play/level/wishing-well?
# You need exactly 104 gold. 

less = "Nimis"
more = "Non satis"
requiredGold = 104

# This function calculates the sum of all coin values.
def sumCoinValues(coins):
    coinIndex = 0
    totalValue = 0
    # Iterate all coins.
    while coinIndex < len(coins):
        totalValue += coins[coinIndex].value
        coinIndex += 1
    return totalValue

def collectAllCoins():
    item = hero.findNearest(hero.findItems())
    while item:
        hero.moveXY(item.pos.x, item.pos.y)
        item = hero.findNearest(hero.findItems())

while True:
    items = hero.findItems()
    # Get the total value of coins.
    goldAmount = sumCoinValues(items)
    # If there are coins, then goldAmount isn't zero.
    if goldAmount != 0:
        # If goldAmount is less than requiredGold
        if goldAmount < requiredGold:
            # Then say "Non satis".
            hero.say("Non satis")
        # If goldAmount is greater than requiredGold
        if goldAmount > requiredGold:
            # Then say "Nimis".
            hero.say("Nimis")
        # If goldAmount is exactly equal to requiredGold
        if goldAmount == requiredGold:
            # Then collect all coins:
            collectAllCoins()
        pass