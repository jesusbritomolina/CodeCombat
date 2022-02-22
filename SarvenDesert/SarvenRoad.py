# https://codecombat.com/play/level/sarven-road?
# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to the current X and Y position.

while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x
    yPos = hero.pos.y
    # If there's an enemy, attack.
    if enemy:
        hero.attack(enemy)
    # Else, keep moving up and to the right. 
    else:
        xPos += 5
        yPos += 5
        hero.moveXY(xPos, yPos)
    pass