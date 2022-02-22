# https://codecombat.com/play/level/dust?
# Use a while to loop until you have counted 10 attacks.

attacks = 0
while attacks < 10:
    enemy = hero.findNearestEnemy()
    # Attack the nearest enemy!
    hero.attack(enemy)
    # Incrementing means to increase by 1.
    # Increment the `attacks` variable.
    attacks += 1

# When you're done, retreat to the ambush point.
hero.moveXY(79, 33)
hero.say("I should retreat!") #∆ Don't just stand there blabbering!