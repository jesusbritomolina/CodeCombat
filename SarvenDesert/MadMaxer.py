# https://codecombat.com/play/level/mad-maxer?
# Ataca al enemigo que está más lejos primero.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Mira a todos los enemigos para descubrir cuál está más lejos.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # ¿Está este enemigo más lejos que lo más lejos que hemos visto hasta ahora?
        distance = hero.distanceTo(target)
        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        # ¡Elimina al enemigo más lejano!
        # Sigue atacando al enemigo mientras su salud sea mayor que 0.
        while farthest.health > 0:
            hero.attack(farthest)
        pass