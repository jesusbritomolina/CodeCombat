# https://codecombat.com/play/level/cavern-survival?
# ¡Sobrevive más que el héroe enemigo!
while True:
    # Planea tu propia estrategia. ¡Se creativo!
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)