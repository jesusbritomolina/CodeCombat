# https://codecombat.com/play/level/the-one-wizard?
# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.

while True:
    enemy = hero.findNearestEnemy()
    
    if enemy:
        distance = hero.distanceTo(enemy)
        if enemy.type == "ogre":
            hero.moveXY(10, 36)  
        elif distance < 10 and hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        elif hero.canCast("lightning-bolt", enemy):
            hero.cast("lightning-bolt", enemy)
        elif hero.canCast("regen", hero) and hero.health < 50:
            hero.cast("regen", hero)
        else:
            hero.attack(enemy)