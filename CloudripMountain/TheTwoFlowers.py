# https://codecombat.com/play/level/the-two-flowers?
# If the peasant is damaged, the flowers will shrink!

def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")

# Define the function: commandSoldiers
def commandSoldiers():
    for soldier in hero.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)
            
# Define the function: pickUpNearestCoin
def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)
peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()