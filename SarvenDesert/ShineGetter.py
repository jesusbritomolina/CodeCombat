# https://codecombat.com/play/level/shine-getter?
# Para obtener la mayor cantidad de oro rápidamente, solo busca las monedas de oro.

while True:
    coins = hero.findItems()
    coinIndex = 0
    
    # Envuelva esto en un bucle que itera sobre todas las monedas.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        # Las monedas de oro valen 3.
        if coin.value == 3:
            # Solo recoge monedas de oro.
            hero.moveXY(coin.pos.x, coin.pos.y)
            pass
        coinIndex += 1