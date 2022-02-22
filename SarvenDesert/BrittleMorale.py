# https://codecombat.com/play/level/brittle-morale?
# Tienes una flecha. ¡Haz que cuente!

# Esto debería devolver al enemigo con la mayor salud.
def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemyIndex = 0
    # Mientras enemyIndex(índiceEnemigo) es menor que la longitud de los enemies(enemigos):
    while enemyIndex < len(enemies):
        # Establecer una variable "enemy"(enemigo) a enemies[enemyIndex](enemigos[índiceEnemigo]).
        enemy = enemies[enemyIndex]
        # Si enemy.health(salud del enemigo) es mayor que strongestHealth(salud más fuerte).
        if enemy.health > strongestHealth:
            # Establece `strongest`(másFuerte) a enemy(enemigo).
            # Establece strongestHealth(saludMásFuerte) a enemy.health(saludDelEnemigo).
            strongest = enemy
            strongestHealth = enemy.health
        # Incrementar enemyIndex
        enemyIndex += 1

    return strongest

enemies = hero.findEnemies()
leader = findStrongestEnemy(enemies)
if leader:
    hero.say(leader)