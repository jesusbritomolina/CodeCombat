# https://codecombat.com/play/level/basin-stampede?
# Sigue hacia la derecha, pero ajusta arriba y abajo a medida que avances.

while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17
    if enemy:
        # Ajusta Y arriba o abajo para escapar de los Yaks.
        if enemy.pos.y > hero.pos.y:
            # Si el Yak está encima tuyo, resta 3 a yPos
            yPos -= 3
            pass
        elif enemy.pos.y < hero.pos.y:
            # Si el Yak está debajo tuyo, agrega 3 a yPos
            yPos += 3
            pass
    hero.moveXY(xPos, yPos)