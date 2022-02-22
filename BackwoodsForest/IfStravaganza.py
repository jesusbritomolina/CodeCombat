# https://codecombat.com/play/level/if-stravaganza?
# ¡Derrota a los ogros desde dentro de su propio campamento!

while True:
    enemy = hero.findNearestEnemy()
    # Usa la sentencia if para comprobar si existe un enemigo:
    if enemy:
        # Ataca al enemigo si existe:
        hero.attack(enemy)
        hero.attack(enemy)