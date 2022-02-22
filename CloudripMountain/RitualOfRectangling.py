# https://codecombat.com/play/level/ritual-of-rectangling?
# We must summon the Ancient Warrior for this ogre!
# Four paladins must form a rectangle.
# But the rectangle needs a specific area and perimeter
# Paladins will keep moving, say the spell when ready.
# It is hard to be precise, but almost equal is good.


# This function should compare valueA and B within 3%.
def almostEqual(valueA, valueB):
    # Check if valueA is > 0.97 and < 1.03 of valueB.
    if valueA > 0.97 * valueB and valueA < 1.03 * valueB:
        return True
    # As a default, just check equality.
    return valueA == valueB

# This function should calculate the perimeter:
def perimeter(side1, side2):
    # The perimeter is the sum of all four sides.
    return (side1 + side2) * 2

# This function should return the area:
def area(side1, side2):
    # The area of a rectangle is the product of 2 sides
    return side1 * side2

# Required summoning values for area and perimeter:
requiredPerimeter = 104
requiredArea = 660

# We will use this unit as a base for our calculations:
base = hero.findNearest(hero.findFriends())

while True:
    sideSN = base.distanceTo("Femae")
    sideWE = base.distanceTo("Illumina")
    currentPerimeter = perimeter(sideSN, sideWE)
    currentArea = area(sideSN, sideWE)
    if almostEqual(currentArea, requiredArea) and almostEqual(currentPerimeter, requiredPerimeter):
        hero.say("VENITE!")
        break