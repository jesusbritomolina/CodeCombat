# https://codecombat.com/play/level/chain-of-command?
# Solo tu mascota puede despertar al mago.

def onHear(event):
    # "hear" events set the event.speaker property.
    # Check if the pet has heard the hero:
    if event.speaker == hero:
        pet.say("WOOF")

# Assign the event handler for "hear" event.
pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    # Si hay un enemigo:
    if enemy:
        # Usa hero.say() para llamar a tu mascota.
        hero.say(pet)
        # Muevete hacia la X en el campo.
        hero.moveXY(30, 33)
        # Then return to the X outside the camp.
        hero.moveXY(30, 15)