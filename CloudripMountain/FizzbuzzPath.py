# https://codecombat.com/play/level/fizzbuzz-path?
# Be aware of hidden traps, and count your steps
# Coins are separated by 10 meters distance

steps = 1

while True:
    # If the number of steps is divisible by 3 AND by 5 -- move to North-West
    if steps % 3 == 0 and steps % 5 != 0:
        hero.moveXY(hero.pos.x + 10, hero.pos.y)
    # Else if the number of steps is divisible by 3 -- move to East
    elif steps % 3 != 0 and steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
    # Else if the number of steps is divisible by 5 -- move to West
    elif steps % 3 == 0 and steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y + 10)
    # Else move to North
    else:
        hero.moveXY(hero.pos.x, hero.pos.y + 10)
    
    steps += 1