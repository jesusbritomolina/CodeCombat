# https://codecombat.com/play/level/underground-business?
# Accumulate 300 gold and escape from the dungeon.

def onSpawn(event):
    # Send the pet to walk around the dungeon:
    pet.moveXY(26, 55)
    pet.moveXY(71, 57)
    pet.moveXY(71, 11)
    pet.moveXY(20, 11)
    pet.moveXY(21, 36)
    pet.moveXY(15, 36)
    # Don't forget to return it to the hero:
    pet.moveXY(hero.pos.x-10, hero.pos.y)
    pass

pet.on("spawn", onSpawn)

while True:
    # Guard peasants:
    enemy = hero.findNearestEnemy()
    # When you have 300+ gold move to the red mark:
    if enemy:
        hero.attack(enemy)
    elif hero.gold >= 300:
        hero.moveXY(50, 34)
    pass