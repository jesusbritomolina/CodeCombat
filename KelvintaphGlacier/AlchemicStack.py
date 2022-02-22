# https://codecombat.com/play/level/alchemic-stack?
# Usa hongos para debilitar al Yeti.
# Usa pociones para curar al héroe.
yeti = hero.findNearestEnemy()
peasant = hero.findFriends()[0]
items = peasant.findItems()

# Use el comando "pickUpItem" para tomar cada elemento.
for item in items:
    if item.type!="gold-key":
        hero.command(peasant, "pickUpItem", item)
# Use el comando "dropItem" para soltar el elemento superior.
# Suelta la llave cerca de la puerta para abrirla.
key = peasant.findNearestByType("gold-key")
hero.command(peasant, "pickUpItem", key)
hero.command(peasant, "dropItem", Vector(40, 36))
# Use peasant.peekItem () para acceder al elemento en la parte superior de la pila.
# Deja setas en el yeti, pociones en el héroe.
while True:
    item = peasant.peekItem()
    if not(item):
        break
    if item.type == "potion":
        hero.command(peasant, "dropItem", hero.pos)
    elif item.type == "mushroom":
        hero.command(peasant, "dropItem", yeti.pos)

# Aaa y uno (o dos) ataques finales para derrotar al yeti.
while True:
    hero.attack(yeti)