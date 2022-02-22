# https://codecombat.com/play/level/blind-distance?
# Dile al mago la distancia de los ogros que se acercan.

# Ésta función encuentra al enemigo más cercano y te dice la distancia a la que se encuentra.
# Si no hay enemigos, la función devuelve un 0.
def nearestEnemyDistance():
    enemy = hero.findNearestEnemy()
    result = 0
    if enemy:
        result = hero.distanceTo(enemy)
    return result

while True:
    # Utiliza la función 'nearestEnemyDistance' y
    # guarda su resultado en la variable 'distance'.
    enemyDistance = nearestEnemyDistance()
    # Si enemyDistance es más que 0:
    if enemyDistance > 0:
        # Di el valor de la variable.
        hero.say(enemyDistance)