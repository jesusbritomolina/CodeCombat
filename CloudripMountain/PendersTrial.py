# https://codecombat.com/play/level/penders-trial?
# Pender wants to test you on a series of trials. Use your boss star to clear off the ogres! Remember, you cannot move or attack in this level.
def summonTroops():
    # These are just an example. Feel free to use griffin riders and/or other units!
    if hero.gold >= 40:
        hero.summon("soldier")
        hero.summon("archer")

def commandPeasant():
    peasant = hero.findByType("peasant")[0]
    if peasant:
        item = peasant.findNearestItem()
        if item:
            hero.command(peasant, "move", item.pos)

def commandSoldiers():
    soldiers = hero.findByType("soldier")
    for soldier in soldiers:
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)

def commandArchers():
    archers = hero.findByType("archer")
    for archer in archers:
        enemy = archer.findNearestEnemy()
        if enemy:
            hero.command(archer, "attack", enemy)

while True:
    summonTroops()
    commandPeasant()
    commandSoldiers()
    commandArchers()
    
    # Iterate over all troops using a for loop. Make peasants collect coins. Combat troops fight.