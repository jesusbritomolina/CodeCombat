# https://codecombat.com/play/level/the-final-kithmaze?
# Usa un solo bucle while-true para moverte y atacar
while True:
    hero.moveRight()
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()