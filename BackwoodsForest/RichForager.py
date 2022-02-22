# https://codecombat.com/play/level/rich-forager?
# Usa  "if" y "else if"  para manipular cualquier situación.
# ¡Ensambla todo para derrotar los enemigos y tomar las monedas!
# ¡Asegúrate de comprar una buena armadura en la tienda de cosas! 400 de vida es lo recomendable.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        # ¿Qué pasa cuando encuentro una bandera?
        hero.pickUpFlag(flag)
    elif enemy:
        # ¿Qué pasa cuando encuentro un enemigo?
        hero.attack(enemy)
    elif item:
        # ¿Qué pasa cuando encuentro un elemento?
        hero.moveXY(item.pos.x, item.pos.y)