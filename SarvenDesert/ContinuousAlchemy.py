# https://codecombat.com/play/level/continuous-alchemy?
# Race munchkins to the water distilled by Omarn Brewstone!
# Use the `continue` statement to avoid poison.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # If there is no enemy, continue out of the loop.
    if not enemy:
        continue
    
    # If there is no item, ask for a potion then continue:
    if not item:
        hero.say("Give me a drink!")
        continue
    
    # If the item.type "poison", continue out of the loop.
    if item.type == "poison":
        continue
    # At this point, the potion must be a bottle of water
    # so moveXY to the potion, then back to the start!
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        hero.moveXY(34, 46)