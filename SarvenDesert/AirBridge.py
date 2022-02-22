# https://codecombat.com/play/level/air-bridge?
# Ayuda a los campesinos a escapar.

def onSpawn(event):
    # Necesitamos salvar tres campesinos.
    remainingPeasants = 3
    while remainingPeasants > 0:
        # Toma una buena posición.
        pet.moveXY(40, 55)
        peasant = pet.findNearestByType("peasant")
        if peasant:
            # Lleva al campesino al pasillo central.
            pet.carryUnit(peasant, 40, 34)
            remainingPeasants -= 1
    munchkin = pet.findNearestByType("munchkin")
    # Lleva a un munchkin a las trampas de fuego.
    if munchkin.maxHealth < 0.1 * hero.maxHealth:
        pet.carryUnit(munchkin, 40, 17)

pet.on("spawn", onSpawn)

# ¡Pelea!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)