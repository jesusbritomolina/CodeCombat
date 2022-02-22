# https://codecombat.com/play/level/medical-attention?
# Ask the healer for help when you're under one-half health.

while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    # Si tu salud actual es menos que el umbral,
    # move to the healing point and say, "heal me".
    # De otra manera, ataca, ¡Necesitaras pelear duro!
    enemy = hero.findNearestEnemy()
    if currentHealth < healingThreshold:
        hero.moveXY(65, 46)
    elif enemy:
        hero.attack(enemy)