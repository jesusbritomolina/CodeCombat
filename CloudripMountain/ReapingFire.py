# https://codecombat.com/play/level/reaping-fire?
# The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

def commandAttack():
    # Command your griffin riders to attack ogres.
    griffinriders = hero.findByType("griffin-rider")
    for griffinrider in griffinriders:
        enemy = griffinrider.findNearestEnemy()
        if enemy:
            hero.command(griffinrider, "attack", enemy)
    pass
    
def pickUpCoin():
    # Collect coins
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    pass
    
def heroAttack():
    # Your hero should attack fang riders that cross the minefield.
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type == "fangrider" and enemy.pos.x < 30:
        hero.attack(enemy)
        hero.attack(enemy)
    pass

def summon():
    if hero.gold > hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")

while True:
    # Call a function, depending on what the current strategy is.
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    summon()
    commandAttack()
    heroAttack()
    pickUpCoin()
    continue