# https://codecombat.com/play/level/guard-dog?
# No puedes ayudar a los campesinos del otro lado del río.
# Pero, tu mascota puede!
# Enseñe a tu lobo a ser un perro de guardia.

def onSpawn(event):
    while True:
        # Las mascotas también pueden encontrar enemigos.
        enemy = pet.findNearestEnemy()
        # Si hay un enemigo:
        if enemy:
            # Entonces debes hacer que el animal diga algo:
            pet.say("Help me!")

pet.on("spawn", onSpawn);