# https://codecombat.com/play/level/teatime?
# Usa temporizadores para generar enemigos y objetos.

# Esto genera dos munchkins agresivos.
def spawnMunchkins():
    munchkin1 = game.spawnXY("munchkin", 2, 12)
    munchkin2 = game.spawnXY("munchkin", 2, 56)
    munchkin1.behavior = "AttacksNearest"
    munchkin2.behavior = "AttacksNearest"

# Esto genera dos throwers agresivos.
def spawnThrowers():
    thrower1 = game.spawnXY("thrower", 2, 16)
    thrower1.behavior = "AttacksNearest"
    thrower2 = game.spawnXY("thrower", 2, 52)
    thrower2.behavior = "AttacksNearest"

# Esto genera una poción de salud cerca del pueblo.
def spawnPotion():
    game.spawnXY("potion-large", 46, 34)

# sobrevive por 30 segundos
game.addSurviveGoal(20)

# Los valores iniciales de los temporizadores definen la primera aparición.
game.munchkinSpawnTime = 0
game.throwerSpawnTime = 0
game.potionSpawnTime = 6
# Esto se usa para la UI(interfaz de usuario).
game.nextPotionIn = 0

ui.track(game, "time")
# Vamos a mostrar cuánto tiempo pasa hasta la próxima poción.
ui.track(game, "nextPotionIn")

player = game.spawnPlayerXY("duelist", 40, 34)
player.maxSpeed = 15

# Esto comprueba y actualiza los temporizadores.
def updateTimers():
    # Si el tiempo de juego es mayor que el munchkinSpawnTime
    if game.time > game.munchkinSpawnTime:
        # Actualiza el temporizador y genera los munchkins.
        game.munchkinSpawnTime = game.munchkinSpawnTime + 6
        spawnMunchkins()
    # Si el tiempo de juego es mayor que potionSpawnTime
    if game.time > game.potionSpawnTime:
        player.say("¡La poción está aquí!")
        # Aumentar game.potionSpawnTime en 6:
        game.potionSpawnTime = game.potionSpawnTime + 6
        # Llame la función spawnPotion:
        spawnPotion()
    # Si el tiempo de juego es mayor que throwerSpawnTime:
    if game.time > game.throwerSpawnTime:
        # Aumentar game.throwerSpawnTime en 9:
        game.throwerSpawnTime += 9
        # Llame a la función spawnThrowers:
        spawnThrowers()
    # Actualiza el temporizador de UI hasta la próxima poción
    game.nextPotionIn = game.potionSpawnTime - game.time
    
while True:
    updateTimers()