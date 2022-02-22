# https://codecombat.com/play/level/bash-em-all?
# Cuidado con estos ogros.
# Son ogros libres de grasa, con entrenamiento especial, y muy fuertes.
# La clave es "libres de grasa"

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    items = hero.findItems()
    itemIndex = 0
    
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        hero.moveXY(40, 33)
        enemyIndex += 1

    while itemIndex < len(items):
        item = items[itemIndex]
        hero.moveXY(item.pos.x, item.pos.y)
        hero.moveXY(40, 33)
        itemIndex += 1