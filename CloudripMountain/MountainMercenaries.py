# https://codecombat.com/play/level/mountain-mercenaries?
# Gather coins to summon soldiers and have them attack the enemy.

while True:
    # Move to the nearest coin.
    # Use move instead of moveXY so you can command constantly.
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    
    # If you have funds for a soldier, summon one.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
        
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        # Loop over all your soldiers and order them to attack.
        while soldierIndex < len(soldiers):
            soldier = soldiers[soldierIndex]
            soldierIndex += 1
            # Use the 'attack' command to make your soldiers attack.
            hero.command(soldier, "attack", enemy)