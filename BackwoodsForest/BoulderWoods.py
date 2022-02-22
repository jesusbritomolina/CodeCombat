# https://codecombat.com/play/level/boulder-woods?
# Use isPathClear to move around the randomly positioned boulders.
# Automatic pathfinding doesn't work in Boulder Woods.
while True:
    angle = Math.PI / 2 - Math.PI / 16
    while angle >= -Math.PI / 2:
        targetX = hero.pos.x + 5 * Math.cos(angle)
        targetY = hero.pos.y + 5 * Math.sin(angle)
        # Use isPathClear between your current `pos` and the target.
        # If the path is clear, move to the target.
        target = (targetX, targetY)
        if (hero.isPathClear(hero.pos, {'x': targetX, 'y': targetY})):
            hero.moveXY(targetX, targetY)
        # Otherwise, sweep the `angle` clockwise a bit.
        else:
            angle -= Math.PI / 16