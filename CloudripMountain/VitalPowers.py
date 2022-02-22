# https://codecombat.com/play/level/vital-powers?
# This level shows how to define your own functions.
# The code inside a function is not executed immediately. It's saved for later.
# This function has your hero collect the nearest coin.
def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)

# This function has your hero summon a soldier.
def summonSoldier():
    # If hero.gold is greater than the cost of the "soldier":
    if hero.gold > hero.costOf("soldier"):
        # Then summon a "soldier":
        hero.summon("soldier")
    pass


# This function commands your soldiers to attack their nearest enemy.
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)

while True:
    # In your loop, you can "call" the functions defined above.
    # The following line causes the code inside the "pickUpNearestCoin" function to be executed.
    pickUpNearestCoin()
    # Call summonSoldier here
    summonSoldier()
    # Call commandSoldiers here
    commandSoldiers()