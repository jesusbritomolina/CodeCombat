# https://codecombat.com/play/level/sand-snakes?
# Este campo está cubierto de firetraps. Afortunadamente, hemos enviado un explorador por delante para encontrar un camino. Dejó las monedas a lo largo del recorrido por lo que si siempre se adhiere a la moneda más cercana, vamos a evitar las trampas.

# ¡Este cañón parece interferir con tus gafas findNearest!
# Tendrás que encontrar las coins más cercanas por tu cuenta.
while True:
    coins = hero.findItems()
    coinIndex = 0
    nearest = None
    nearestDistance = 9999
    
    # Recorre todas las coins para encontrar la más cercana.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        # Si distance de coin es menor que la nearestDistance
        if distance < nearestDistance:
            # asigna nearest a coin
            nearest = coin
            # asigna nearestDistance a distance
            nearestDistance = distance
            
    # Si hay una moneda más cercana, muévase a su posición. Necesitarás moveXY para no cortar esquinas y golpear una trampa.
    if nearest:
        hero.moveXY(nearest.pos.x, nearest.pos.y)