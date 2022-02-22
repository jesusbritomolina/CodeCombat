# https://codecombat.com/play/level/double-agent?
# Encuentra el numero escondido en el mensaje del agente para escapar.
# Cuenta el numero de espacios en blanco al comienzo y al final.

# Esta funcion regresa a las coordinadas de la ruta n-th.
def passagePosByNum(n):
    return {"x": 60, "y": n * 12 + 8}

def onHear(event):
    # Mensaje original.
    message = event.message
    # Corta el mensaje:
    messages = message.trim(" ")
    # El numero escondido es la diferencia de longitud:
    number = len(message)-len(messages)
    pet.say(number)
    # Usa passagePosByNum para encontrar la ruta para entrar:
    pos = passagePosByNum(number)
    # Mueve la mascota a la entrada de la ruta:
    pet.moveXY(pos.x, pos.y)
    # Mueve la mascota a la izquierda del borde del mapa:
    pet.moveXY(0, pos.y)

pet.on("hear", onHear)

# El heroe debe seguir a la mascota.
while True:
    hero.move(pet.pos)