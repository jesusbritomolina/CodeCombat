# https://codecombat.com/play/level/polygonception?
# You are on your own this time, I hope you have learned what you need from the previous fractal levels. Check the guide for help with what you need to do and with the math required for polygons.

# You need a function to convert degrees to radians.  Multiply degrees by Math.PI / 180.
def degreesToRadians(degrees):
    return Math.PI / 180 * degrees

# Your polygon function should have 3 inputs: start, end, and sides.
def polygon(start_, end_, side):
    start = start_
    end = end_
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    hero.toggleFlowers(False)
    hero.moveXY(start.x, start.y)
    hero.toggleFlowers(True)
    for i in range(side):
        hero.moveXY(end.x, end.y)
        full = Vector.rotate(full, degreesToRadians(360 / side))
        if distance > 10:
            polygon(end, Vector.add(end, Vector.divide(full, 5)), side)
        end = Vector.add(end, full)
# Remember to make your polygon recursive, drawing extra polygons at every corner.
# To get the start and end position for each polygon, add startOffset and endOffset to the yak's position.
startOffset = Vector(-15, -15)
endOffset = Vector(15, -15)

# You need to loop through all the yaks, drawing a polygon for each.  Yaks are enemies.
startOffset = Vector(-15, -15)
endOffset = Vector(15, -15)
enemies = self.findEnemies()
for enemy in enemies:
    start = Vector.add(enemy.pos, startOffset)
    end = Vector.add(enemy.pos, endOffset)
    sides = enemy.sides
    polygon(start, end, sides)