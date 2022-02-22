# https://codecombat.com/play/level/alchemic-power?
# Espera los comandos del alquimista para buscar pociones.

# El controlador de eventos para el evento "hear"(oír) de la mascota. 
def onHear(event):
    # Encuentra la poción más cercana.
    potion = pet.findNearestByType("potion")
    message = event.message
    # Si el mensaje del evento es "Fetch"(trae)
    if message == "Fetch":
        # Haz que la mascota busque la poción.
        pet.fetch(potion)
    # Si no (para cualquier otro mensaje):
    else:
        # Usa pet.moveXY(mascota.mueveteXY) para devolver a la mascota a la marca roja.
        pet.moveXY(54, 34)

pet.on("hear", onHear)

# No tienes que cambiar el código que se encuentra a continuación.
while True:
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(40, 34)