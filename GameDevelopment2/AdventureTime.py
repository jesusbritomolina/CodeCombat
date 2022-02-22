# https://codecombat.com/play/level/adventure-time?
# "tiempo.juego" es el tiempo que ha pasado en el juego.
game.spawnPlayerXY("guardian", 10, 35)
game.addSurviveGoal()
game.addDefeatGoal(5)

def onSpawn(event):
    while True:
        unit = event.target
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

game.setActionFor("munchkin", "spawn", onSpawn)

# "tiempo.juego" empieza en 0, y empieza a aumentar en segundos.
spawnTime = 0
while True:
    # SpawnTime es el tiempo que queremos para generar un nuevo enemigo.
    if game.time > spawnTime:
        pass
        # Genera un "munchkin" en (60,35)
        game.spawnXY("munchkin", 60, 35)
        # Situa spawnTime igual al game.time más 2 segundos.
        # Un enemigo aparecerá cada 2 segundos.
        spawnTime = game.time + 2