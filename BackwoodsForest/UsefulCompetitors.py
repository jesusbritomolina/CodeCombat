# https://codecombat.com/play/level/useful-competitors?
# El campo de monedas ha sido sembrado con frascos de veneno mortal.
# ¡Los ogros están atacando, mientras que sus peones están tratando de robar sus monedas!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Ataca al enemigo solo si el tipo NO es igual a "peon".
        if enemy.type != "peon":
            hero.attack(enemy)
    item = hero.findNearestItem()
    if item:
        # Reúna el elemento sólo si el tipo NO es igual a "veneno".
        if item.type != "poison":
            hero.moveXY(item.pos.x, item.pos.y)
        pass