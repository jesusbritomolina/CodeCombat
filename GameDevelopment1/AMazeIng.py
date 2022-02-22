# https://codecombat.com/play/level/a-maze-ing?
# A Alejandro le gusta el reto!
# Añade más objetos "forest" (bosque) al nivel para crear un laberinto largo.

# Establecer el objetivo del juego.
game.addCollectGoal()
# Selecciona un héroe y genera cofres para recolectar.
game.spawnPlayerXY("duelist", 9, 59)
game.spawnXY("chest", 8, 14)

game.spawnXY("forest", 26, 51)
# Añade 2 objetos "forest" mas. Asegúrate de no bloquear las gemas por completo!
game.spawnXY("forest", 50, 21)
game.spawnXY("forest", 34, 22)