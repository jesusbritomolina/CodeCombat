# https://codecombat.com/play/level/airdrop?
# Coge todas las espadas y protege la villa.

def onSpawn (event):
    while True:
        item = hero.findNearestItem()
        #  La mascota debe alcanzar el item si este existe:
        if item:
            pet.fetch(item)

# Asigna una función onSpawn  para el "spawn" de la mascota.
pet.on("spawn", onSpawn)

while True:
    # Protege el pasaje izquierdo:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    pass