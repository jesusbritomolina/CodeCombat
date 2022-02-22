# https://codecombat.com/play/level/alpine-rally?
# Escapar del lado derecho del mapa.
# Para correr más rápido que el yeti, tendrás que hacerte más rápido.
# Usar resetCooldown para usar un hechizo o habilidad con más frecuencia.
# manaBlast puede ayudar a despejar el camino.

hero.cast("haste", self)
hero.cast("invisibility", self)
hero.moveXY(105, 36)
hero.cast("gold-shield", self)

hero.moveXY(169, 36)

hero.cast("haste", self)
hero.cast("invisibility", self)
hero.moveXY(302, 36)