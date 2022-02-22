# https://codecombat.com/play/level/bank-raid?
# Espera a los ogros, derrótalos y recoge oro.

while True:
    enemies = hero.findEnemies()
    # Se usa enemyIndex para repetir el array de enemigos.
    enemyIndex = 0
    # Minetras que enemyIndex sea menor que len(enemies)
    while enemyIndex < len(enemies):
        # Ataque al enemigo en coinIndex.
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        # Incrementa coinIndex por uno.
        enemyIndex += 1
    coins = hero.findItems()
    # Se usa coinIndex para repetir el array de monedas.
    coinIndex = 0
    while coinIndex < len(coins):
        # Consigue una moneda del array de monedas usando coinIndex.
        coin = coins[coinIndex]
        # Recoge esa moneda.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Incrementa coinIndex por uno.
        coinIndex += 1