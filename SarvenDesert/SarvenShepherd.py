# https://codecombat.com/play/level/sarven-shepherd?
# Use los bucles while para elegir el ogro

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0

    # Envuelve esta lógica en un bucle while para atacar a todos los enemigos.
    # Encuentra la longitud de la array con: len(enemies)
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # "!=" significa "no es igual a".
        if enemy.type != "sand-yak":
            # Mientras la salud del enemigo es mayor que 0, ¡ataca!
            while enemy.health > 0:
                hero.attack(enemy)
            pass
        enemyIndex += 1
    
    # Entre oleadas, vuelve al centro.
    hero.moveXY(40, 32)