# https://codecombat.com/play/level/bombing-run?
# Incoming oscars! (That's military speak for ogres).
# You will need to calculate their angle of attack.
# Use that angle to command your Griffin Bombers!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Find the vector of attack
        O = Math.abs(enemy.pos.y - hero.pos.y)
        A = Math.abs(enemy.pos.x - hero.pos.x)
        angle = Math.atan2(O, A)
        angle = angle * 180 / Math.PI
        if enemy.pos.x < hero.pos.x:
            angle = 180 - angle
        hero.say(angle)
        # Use trigonometry to find the the angle in Radians!
        # The answer must be in Degrees!
        # To convert Radians to Degrees multiply by (180 / Math.PI)
        # Say the angle!