# https://codecombat.com/play/level/team-work?
# Las gemas desaparecerán pronto. ¡Necesitarás ayuda!

# findItems() devuelve una array de elementos.
items = hero.findItems()

# Consigue la primera gema de la array.
# No olvides que el primer índice es 0.
gem0 = items[0]

# Dile a Bruno que consiga gem0
hero.say("Bruno " + gem0)

# Puedes hacer referencia a la gema sin una variable.
hero.say("Matilda " + items[1])

# Crea una variable para la última gema, items[2]:
gem2 = items[2]
# Muévete a la posición de esa gema usando moveXY()
hero.moveXY(gem2.pos.x, gem2.pos.y)