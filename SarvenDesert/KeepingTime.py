# https://codecombat.com/play/level/keeping-time?
# Use your new skill to choose what to do: hero.time

while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # If it's the first 10 seconds, attack.
    if hero.time < 10:
        hero.attack(enemy)
        pass
    # Else, if it's the first 35 seconds, collect coins.
    elif hero.time < 35:
        hero.moveXY(item.pos.x, item.pos.y)
        pass
    # After 35 seconds, attack again!
    else:
        hero.attack(enemy)
        pass