# https://codecombat.com/play/level/black-diamond?
while True:
    gem = hero.findNearest(hero.findItems())
    if gem:
        clear = hero.isPathClear(hero.pos, gem.pos)
        # The isPathClear method tells you if there’s an obstacle in the way.
        # If it’s clear, move() to gem.pos.
        if clear:
            hero.move(gem.pos)
        # Else, move back to the center point.
        else:
            hero.move({"x": 40, "y": 35})