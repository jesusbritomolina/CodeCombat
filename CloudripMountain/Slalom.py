# https://codecombat.com/play/level/slalom?
# Usa objetos literales para recorrer el camino seguro y recoger las gemas.
# ¡No podes usar moveXY() en este nivel! Usa move() para moverte.
gems = hero.findItems()

while hero.pos.x < 20:
	# move() acepta objetos con propiedades ' x ' e ' y ', no solo números.
	hero.move({'x': 20, 'y': 35})

while hero.pos.x < 25:
	# La posición de una gema es un objeto con propiedades ' x ' e ' y '.
	gem0 = gems[0]
	hero.move(gem0.pos)

# Mientras tu ' x ' es menor que 30,
# Usa un objeto para moverte a 30, 35.
while hero.pos.x < 30:
    hero.move({'x': 30, 'y': 35})
# Mientras tu ' x ' es menor que 35,
# Muevete hacia la posición de gems[1].
while hero.pos.x < 35:
    gem1 = gems[1]
    hero.move(gem1.pos)
while hero.pos.x < 40:
    hero.move({'x': 40, 'y': 35})
# ¡Hazte hasta el último par de gemas!
while hero.pos.x < 45:
    gem2 = gems[2]
    hero.move(gem2.pos)
while hero.pos.x < 50:
    hero.move({'x': 50, 'y': 35})
while hero.pos.x < 55:
    gem3 = gems[3]
    hero.move(gem3.pos)