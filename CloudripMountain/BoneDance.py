# https://codecombat.com/play/level/bone-dance?
# Soothe the skeletons when they get too close.

# This function is useful to compare float numbers.
def almostEqual(a, b):
    return Math.abs(a - b) < 1

while True:
    skeleton = hero.findNearestEnemy()
    # Find the radius of the skeleton circle.
    radius = hero.distanceTo(skeleton)
    # If the circumference is almost equal 100:
    length = 2*radius*Math.PI
    if almostEqual(length, 100):
        # Say, sing, or shout anything once.
        hero.say('ALARM!')